from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Article

User = get_user_model()

class ArticleListSerializer(serializers.ModelSerializer):
    
    author = serializers.ReadOnlyField(source='user.username')
    author_id = serializers.ReadOnlyField(source='user.id')
    likes_count = serializers.IntegerField(source='liked_users.count', read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'image', 'author', 'author_id', 'created_at', 'likes_count')


class ArticleSerializer(serializers.ModelSerializer):
    
    author = serializers.ReadOnlyField(source='user.username')
    author_id = serializers.ReadOnlyField(source='user.id')
    
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user', 'liked_users')
