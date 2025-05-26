import requests
from rest_framework.views    import APIView        # ← 누락됐던 import
from rest_framework.response import Response
from rest_framework          import status

from .services.tmdb import _get
from .serializers   import TMDBMovieSerializer
from .models        import Genre


# ────────────────────────────────
# 1) 장르별 / 전체 영화 목록
#    GET /api/v1/movies/?genre=<name>&page=1
#    GET /api/v1/movies/?genreId=<tmdb_id>&page=1
# ────────────────────────────────
class TMDBMovieListAPI(APIView):
    def get(self, request):
        genre_name = request.GET.get('genre')
        genre_id   = request.GET.get('genreId')
        page       = request.GET.get('page', 1)

        params = {'page': page}
        if genre_id:
            params['with_genres'] = genre_id
        elif genre_name:
            try:
                g = Genre.objects.get(name__iexact=genre_name)
                params['with_genres'] = g.tmdb_id
            except Genre.DoesNotExist:
                pass

        data = _get('discover/movie', **params)
        return Response(data, status=status.HTTP_200_OK)


# ────────────────────────────────
# 2) 영화 상세
#    GET /api/v1/movies/<tmdb_id>/
# ────────────────────────────────
class TMDBMovieDetailAPI(APIView):
    def get(self, request, tmdb_id):
        try:
            # credits 정보까지 함께 가져오려면 append_to_response 옵션 추가
            raw = _get(
                f'movie/{tmdb_id}',
                append_to_response='credits'
            )
        except requests.HTTPError:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # Serializer 검증 없이, TMDB에서 받은 원본 JSON을 그대로 반환
        return Response(raw, status=status.HTTP_200_OK)




# ────────────────────────────────
# 3) 평점 상위 3편 (Now Trending)
#    GET /api/v1/movies/top/?page=1
# ────────────────────────────────
class TMDBTopRatedAPI(APIView):
    def get(self, request):
        page  = request.GET.get('page', 1)
        data  = _get('movie/top_rated', page=page)
        data['results'] = data['results'][:10]      # 처음 3편만
        return Response(data, status=status.HTTP_200_OK)
