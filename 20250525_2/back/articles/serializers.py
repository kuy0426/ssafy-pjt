from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Article

User = get_user_model()

class ArticleListSerializer(serializers.ModelSerializer):
    
    author = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'image', 'author', 'created_at')


class ArticleSerializer(serializers.ModelSerializer):
    
    author = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user', 'liked_users')
