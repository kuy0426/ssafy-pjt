# movies/models.py

from django.db import models
from django.conf import settings

class Genre(models.Model):
    tmdb_id = models.IntegerField(primary_key=True)
    name    = models.CharField(max_length=50)

    class Meta:
        db_table = 'genre'
    def __str__(self):
        return self.name


class Actor(models.Model):
    tmdb_id       = models.IntegerField(primary_key=True)
    name          = models.CharField(max_length=50)
    birthday      = models.DateField(null=True, blank=True)
    place_of_birth= models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'actor'
    def __str__(self):
        return self.name


class Movie(models.Model):
    tmdb_id      = models.IntegerField(primary_key=True)
    original_title = models.CharField(max_length=128)
    description    = models.TextField()
    vote_average   = models.DecimalField(max_digits=5, decimal_places=2)
    release_date   = models.DateField(null=True, blank=True)
    runtime        = models.IntegerField(default=0, help_text='분 단위')

    genres      = models.ManyToManyField(Genre, through='MovieGenre',   related_name='movies')
    actors      = models.ManyToManyField(Actor, through='MovieActor',   related_name='movies')
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                         through='MovieLikeUsers',
                                         related_name='liked_movies')

    class Meta:
        db_table = 'movie'
    def __str__(self):
        return self.original_title


class MovieGenre(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        db_table = 'movie_genre'
        unique_together = (('movie', 'genre'),)
    def __str__(self):
        return f"{self.movie} ↔ {self.genre}"


class MovieActor(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)

    class Meta:
        db_table = 'movie_actor'
        unique_together = (('movie', 'actor'),)
    def __str__(self):
        return f"{self.movie} ↔ {self.actor}"


class MovieLikeUsers(models.Model):
    user       = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie      = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'movie_like_users'
        unique_together = (('user', 'movie'),)
    def __str__(self):
        return f"{self.user} liked {self.movie}"
