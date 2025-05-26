# back/movies/serializers.py

from rest_framework import serializers

class TMDBMovieSerializer(serializers.Serializer):
    # TMDB에서 내려주는 'id' 필드를 그대로 사용합니다.
    id              = serializers.IntegerField()
    original_title  = serializers.CharField()
    overview        = serializers.CharField(allow_blank=True, allow_null=True)
    vote_average    = serializers.FloatField()
    release_date    = serializers.CharField(allow_blank=True, allow_null=True)
    poster_path     = serializers.CharField(allow_null=True)

    # DetailView에서 cast를 별도로 JSON에 붙여주기 때문에 여기에 정의하지 않습니다.
