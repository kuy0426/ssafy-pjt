# back/movies/urls.py

from django.urls import path
from .views import (
    TMDBMovieListAPI,
    TMDBMovieDetailAPI,
    TMDBTopRatedAPI,
    TrendingMoviesAPI,

)

urlpatterns = [

   path('',                TMDBMovieListAPI.as_view(),     name='tmdb-list'),
    path('trending/',       TrendingMoviesAPI.as_view(),    name='tmdb-trending'),
    path('top/',            TMDBTopRatedAPI.as_view(),      name='tmdb-top'),
    path('<int:tmdb_id>/',  TMDBMovieDetailAPI.as_view(),   name='tmdb-detail'),
 ]
