# back/movies/models.py

from django.db import models
from django.conf import settings

class Genre(models.Model):
    """
    TMDB 장르 정보를 저장합니다.
    """
    tmdb_id = models.IntegerField(primary_key=True)
    name    = models.CharField(max_length=50)

    class Meta:
        db_table = 'genre'
        verbose_name = '장르'
        verbose_name_plural = '장르 목록'

    def __str__(self):
        return self.name


class Actor(models.Model):
    """
    TMDB 배우(사람) 정보를 저장합니다.
    """
    tmdb_id        = models.IntegerField(primary_key=True)
    name           = models.CharField(max_length=100)
    birthday       = models.DateField(null=True, blank=True)
    place_of_birth = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        db_table = 'actor'
        verbose_name = '배우'
        verbose_name_plural = '배우 목록'

    def __str__(self):
        return self.name


class Movie(models.Model):
    """
    TMDB 영화 정보를 저장합니다.
    """
    tmdb_id        = models.IntegerField(primary_key=True)
    original_title = models.CharField(max_length=200)
    description    = models.TextField(blank=True)
    vote_average   = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    release_date   = models.DateField(null=True, blank=True)
    runtime        = models.IntegerField(default=0, help_text='분 단위 상영 시간')
    poster_path    = models.CharField(max_length=200, null=True, blank=True)

    # M2M 관계: 영화 ↔ 장르, 영화 ↔ 배우
    genres = models.ManyToManyField(Genre, through='MovieGenre',   related_name='movies')
    actors = models.ManyToManyField(Actor, through='MovieActor',   related_name='movies')

    # (선택) 사용자 좋아요 기능
    liked_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='MovieLikeUsers',
        related_name='liked_movies'
    )

    class Meta:
        db_table = 'movie'
        verbose_name = '영화'
        verbose_name_plural = '영화 목록'

    def __str__(self):
        return self.original_title


class MovieGenre(models.Model):
    """
    영화 ↔ 장르 중간 테이블
    """
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        db_table = 'movie_genre'
        unique_together = (('movie', 'genre'),)
        verbose_name = '영화-장르 연결'
        verbose_name_plural = '영화-장르 연결 목록'

    def __str__(self):
        return f"{self.movie.original_title} ⇄ {self.genre.name}"


class MovieActor(models.Model):
    """
    영화 ↔ 배우 중간 테이블
    """
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)

    class Meta:
        db_table = 'movie_actor'
        unique_together = (('movie', 'actor'),)
        verbose_name = '영화-배우 연결'
        verbose_name_plural = '영화-배우 연결 목록'

    def __str__(self):
        return f"{self.movie.original_title} ⇄ {self.actor.name}"


class MovieLikeUsers(models.Model):
    """
    영화 좋아요 기능을 위한 중간 테이블 (선택)
    """
    user       = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie      = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'movie_like_users'
        unique_together = (('user', 'movie'),)
        verbose_name = '영화 좋아요'
        verbose_name_plural = '영화 좋아요 목록'

    def __str__(self):
        return f"{self.user.username} ❤ {self.movie.original_title}"
