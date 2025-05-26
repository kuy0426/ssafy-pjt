# back/movies/serializers.py
from rest_framework import serializers

class TMDBMovieSerializer(serializers.Serializer):
    tmdb_id        = serializers.IntegerField(source='id')
    original_title = serializers.CharField()
    description    = serializers.CharField(source='overview', allow_blank=True)
    vote_average   = serializers.FloatField()
    # ''(빈 문자열)·null 모두 허용하기 위해 CharField 사용
    release_date   = serializers.CharField(allow_blank=True, allow_null=True)
    poster_path    = serializers.CharField(allow_null=True)
