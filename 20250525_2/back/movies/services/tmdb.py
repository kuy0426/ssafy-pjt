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
