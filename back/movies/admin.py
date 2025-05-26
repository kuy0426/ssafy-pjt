from django.contrib import admin
from .models import Movie, Genre, Actor, MovieGenre, MovieActor, MovieLikeUsers

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('original_title','tmdb_id','release_date','vote_average')
    filter_horizontal = ('genres','actors','liked_users')

admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(MovieGenre)
admin.site.register(MovieActor)
admin.site.register(MovieLikeUsers)
