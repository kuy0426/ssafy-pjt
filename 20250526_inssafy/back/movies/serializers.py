# # back/movies/serializers.py
# from rest_framework import serializers

# class MovieSerializer(serializers.Serializer):

#     id              = serializers.IntegerField()
#     original_title  = serializers.CharField()
#     overview        = serializers.CharField(allow_blank=True, allow_null=True)
#     vote_average    = serializers.FloatField()
#     release_date    = serializers.CharField(allow_blank=True, allow_null=True)
#     poster_path     = serializers.CharField(allow_null=True)


# back/movies/serializers.py

from rest_framework import serializers


class TMDBMovieSerializer(serializers.Serializer):
    id             = serializers.IntegerField()
    original_title = serializers.CharField()
    overview       = serializers.CharField(allow_blank=True, allow_null=True)
    vote_average   = serializers.FloatField()
    release_date   = serializers.CharField(allow_blank=True, allow_null=True)
    poster_path    = serializers.CharField(allow_null=True)


class MovieSerializer(serializers.Serializer):
    id             = serializers.IntegerField()
    original_title = serializers.CharField()
    overview       = serializers.CharField(allow_blank=True, allow_null=True)
    vote_average   = serializers.FloatField()
    release_date   = serializers.CharField(allow_blank=True, allow_null=True)
    poster_path    = serializers.CharField(allow_null=True)