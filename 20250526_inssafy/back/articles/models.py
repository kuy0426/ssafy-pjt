from django.db import models
from django.conf import settings
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=400)
    image = models.ImageField(blank=True, null=True, upload_to='articles/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_articles', through='ArticleLike')
    

class ArticleLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
