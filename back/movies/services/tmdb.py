# movies/services/tmdb.py

import requests
from django.conf import settings
from ..models import Movie, Genre, Actor, MovieGenre, MovieActor

BASE_URL = settings.TMDB_BASE_URL
API_KEY  = settings.TMDB_API_KEY
LANG     = settings.TMDB_LANGUAGE

def _get(path: str, **params) -> dict:
    """TMDB API GET 호출 (내부용)"""
    url = f"{BASE_URL}/{path}"
    params.update({'api_key': API_KEY, 'language': LANG})
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    return resp.json()


def sync_actor(tmdb_id: int) -> Actor:
    """
    TMDB person/{id} 에서 배우 상세 정보(+출생일·출생지)를 불러와 저장/업데이트
    """
    data = _get(f"person/{tmdb_id}")
    actor, _ = Actor.objects.update_or_create(
        tmdb_id=tmdb_id,
        defaults={
            'name'          : data.get('name', ''),
            'birthday'      : data.get('birthday'),
            'place_of_birth': data.get('place_of_birth'),
        }
    )
    return actor


def sync_movie(tmdb_id: int) -> Movie:
    """
    영화 상세 정보 + 전체 크레딧(출연진) 동기화
    """
    # 1) 영화 기본 정보
    data = _get(f"movie/{tmdb_id}")
    movie, _ = Movie.objects.update_or_create(
        tmdb_id=tmdb_id,
        defaults={
            'original_title': data.get('original_title', ''),
            'description'   : data.get('overview', ''),
            'vote_average'  : data.get('vote_average', 0),
            'release_date'  : data.get('release_date') or None,
            'runtime'       : data.get('runtime') or 0,
        }
    )

    # 2) 장르 동기화
    for g in data.get('genres', []):
        genre, _ = Genre.objects.update_or_create(
            tmdb_id=g['id'],
            defaults={'name': g['name']}
        )
        MovieGenre.objects.get_or_create(movie=movie, genre=genre)

    # 3) 출연진(전체) 동기화
    credits = _get(f"movie/{tmdb_id}/credits")
    for c in credits.get('cast', []):
        actor = sync_actor(c['id'])
        MovieActor.objects.get_or_create(movie=movie, actor=actor)

    return movie


def discover_movies(page: int = 1) -> list:
    """
    discover/movie (인기 기준) 결과 리스트를 한 페이지씩 가져옴.
    """
    data = _get("discover/movie", page=page)
    return data.get('results', [])


def sync_popular(max_pages: int = 1):
    """
    인기 영화 목록을 max_pages 페이지만큼 동기화.
    영화당 전체 출연진을 함께 가져옴.
    """
    for p in range(1, max_pages + 1):
        for item in discover_movies(page=p):
            sync_movie(item['id'])
