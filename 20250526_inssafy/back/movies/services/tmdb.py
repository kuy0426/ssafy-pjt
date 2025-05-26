# back/movies/services/tmdb.py

import requests
from django.conf import settings
from typing import List, Dict

from ..models import Movie, Genre, Actor, MovieGenre, MovieActor

# 환경설정
BASE_URL = settings.TMDB_BASE_URL
API_KEY  = settings.TMDB_API_KEY
LANG     = settings.TMDB_LANGUAGE  # ex: 'ko-KR'

def _get(path: str, **params) -> Dict:
    """
    TMDB API GET 헬퍼
    """
    url = f"{BASE_URL}/{path}"
    params.update({'api_key': API_KEY, 'language': LANG})
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    return resp.json()


# ... (sync_movie, popular_ids, sync_popular 등 기존 함수들은 그대로 두세요)


def trending_ids(time_window: str = 'week') -> List[int]:
    data = _get(f"trending/movie/{time_window}")
    return [m['id'] for m in data.get('results', [])]


def get_trending_movies(time_window: str = 'week', limit: int = 10) -> List[Dict]:
    """
    Top 10 Trending Movies 간략 정보 리스트를 반환
    """
    # 1) TMDB에서 원본 결과 가져오기
    data = _get(f"trending/movie/{time_window}")
    results = data.get('results', [])[:limit]

    # 2) 필요한 필드만 추출 — serializer 가 기대하는 key 이름 맞추기
    return [
        {
            'id'            : m.get('id'),
            'title'         : m.get('title') or m.get('name'),
            'overview'      : m.get('overview', ''),
            'vote_average'  : m.get('vote_average', 0),   # ← 반드시 이 key 로
            'release_date'  : m.get('release_date') or '',
            'poster_path'   : m.get('poster_path'),
        }
        for m in results
    ]

def sync_movie(tmdb_id: int) -> Movie:
    """영화 + 장르 + 배우를 DB에 저장/업데이트하고 Movie 인스턴스를 반환"""
    # 1) 영화 기본 정보
    data = _get(f"movie/{tmdb_id}")
    movie, _ = Movie.objects.update_or_create(
        tmdb_id=tmdb_id,
        defaults={
            'original_title': data.get('original_title', ''),
            'description'   : data.get('overview', ''),
            'vote_average'  : data.get('vote_average', 0),
            'release_date'  : data.get('release_date') or None,
            'runtime'       : data.get('runtime', 0),
            'poster_path'   : data.get('poster_path'),
        }
    )

    # 2) 장르 매핑
    for g in data.get('genres', []):
        genre, _ = Genre.objects.update_or_create(
            tmdb_id=g['id'],
            defaults={'name': g['name']}
        )
        MovieGenre.objects.get_or_create(movie=movie, genre=genre)

    # 3) 출연진 전체 매핑
    credits = _get(f"movie/{tmdb_id}/credits")
    for c in credits.get('cast', []):
        actor, _ = Actor.objects.update_or_create(
            tmdb_id=c['id'],
            defaults={'name': c['name']}
        )
        MovieActor.objects.get_or_create(movie=movie, actor=actor)

    return movie

def popular_ids(page: int = 1) -> list[int]:
    """
    인기 영화 1페이지(기본 20편)의 TMDB ID 목록만 반환
    """
    data = _get("movie/popular", page=page)
    return [m["id"] for m in data.get("results", [])]

def sync_popular(max_pages: int = 3):
    """
    인기 영화 max_pages 페이지를 순회하며 DB에 저장
    (max_pages=3 → 약 60편, =5 → 약 100편)
    """
    for p in range(1, max_pages + 1):
        for mid in popular_ids(p):
            sync_movie(mid)          # 이미 작성해 둔 함수