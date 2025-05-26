# movies/services/tmdb.py
import requests
from django.conf import settings
from ..models import Movie, Genre, Actor, MovieGenre, MovieActor

BASE_URL = settings.TMDB_BASE_URL
API_KEY  = settings.TMDB_API_KEY
LANG     = settings.TMDB_LANGUAGE

def _get(path: str, **params) -> dict:
    """TMDB API GET 헬퍼"""
    url = f"{BASE_URL}/{path}"
    params.update({'api_key': API_KEY, 'language': LANG})
    r = requests.get(url, params=params)
    r.raise_for_status()
    return r.json()

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