from django.urls import path
from .views import movie_list, movie_detail, fetch_movies

urlpatterns = [
    path('movies/', movie_list, name='movie_list'),
    path('movies/<int:movie_id>/', movie_detail, name='movie_detail'),
    path('fetch-movies/', fetch_movies, name='fetch_movies'),  # 추가된 엔드포인트
]
