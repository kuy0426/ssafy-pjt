# back/movies/views.py

import requests
from rest_framework.views    import APIView
from rest_framework.response import Response
from rest_framework          import status

from .services.tmdb    import _get, get_trending_movies
from .serializers      import TMDBMovieSerializer
from .models           import Genre


class TMDBMovieListAPI(APIView):
    """
    GET /api/v1/movies/?genre=<name>&genreId=<tmdb_id>&page=1
    → Discover/movie 원본 JSON 그대로 반환
    """
    def get(self, request):
        genre_name = request.GET.get('genre')
        genre_id   = request.GET.get('genreId')
        page       = request.GET.get('page', 1)

        params = {"page": page}
        if genre_id:
            params["with_genres"] = genre_id
        elif genre_name:
            try:
                g = Genre.objects.get(name__iexact=genre_name)
                params["with_genres"] = g.tmdb_id
            except Genre.DoesNotExist:
                return Response({"results": []}, status=status.HTTP_200_OK)

        try:
            raw = _get("discover/movie", **params)
        except requests.HTTPError:
            return Response({"results": []}, status=status.HTTP_200_OK)

        return Response(raw, status=status.HTTP_200_OK)


class TrendingMoviesAPI(APIView):
    """
    GET /api/v1/movies/trending/  → Top 10 Trending Movies
    """
    def get(self, request):
        movies = get_trending_movies(time_window='week', limit=10)
        return Response(movies, status=status.HTTP_200_OK)


class TMDBTopRatedAPI(APIView):
    """
    GET /api/v1/movies/top/?page=1  → 평점 상위 3편
    """
    def get(self, request):
        page = request.GET.get("page", 1)
        raw  = _get("movie/top_rated", page=page)
        top3 = raw.get("results", [])[:3]
        serializer = TMDBMovieSerializer(data=top3, many=True)
        serializer.is_valid(raise_exception=True)
        return Response({**raw, "results": serializer.data}, status=status.HTTP_200_OK)


class TMDBMovieDetailAPI(APIView):
    """
    GET /api/v1/movies/<tmdb_id>/
    → 영화 상세 정보 + cast(출연진) + videos(예고편) 반환
    """
    def get(self, request, tmdb_id):
        try:
            movie   = _get(f"movie/{tmdb_id}")
            credits = _get(f"movie/{tmdb_id}/credits")
            videos  = _get(f"movie/{tmdb_id}/videos")
        except requests.HTTPError:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # cast 리스트 붙이기
        movie["cast"] = credits.get("cast", [])
        # 예고편(videos) 리스트 붙이기
        movie["videos"] = videos.get("results", [])

        # 기본 필드 검증
        serializer = TMDBMovieSerializer(data=movie)
        serializer.is_valid(raise_exception=True)
        data = serializer.data

        # 추가 필드(검증 제외) 세팅
        data["cast"]   = movie["cast"]
        data["videos"] = movie["videos"]

        return Response(data, status=status.HTTP_200_OK)
