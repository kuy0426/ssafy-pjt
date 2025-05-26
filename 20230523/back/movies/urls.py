# back/movies/urls.py
from django.urls import path
from .views import (
    TMDBMovieListAPI,
    TMDBMovieDetailAPI,
    TMDBTopRatedAPI,
)

urlpatterns = [
    path('',              TMDBMovieListAPI.as_view(),    name='tmdb-list'),
    path('<int:tmdb_id>/', TMDBMovieDetailAPI.as_view(), name='tmdb-detail'),
    path('top/',          TMDBTopRatedAPI.as_view(),     name='tmdb-top'),
]
