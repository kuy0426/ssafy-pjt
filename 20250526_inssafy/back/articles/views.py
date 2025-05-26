from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, permissions

# Permissions
from rest_framework.decorators import permission_classes

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import ArticleSerializer, ArticleListSerializer
from .models import Article

@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def article_list(request):
    if request.method == 'GET':
        # 1) ?user=ID 가 있으면 그 유저의 글만,
        #    없으면 전체 글
        user_id = request.query_params.get('user', None)
        if user_id is not None:
            articles = Article.objects.filter(user__id=user_id)
        else:
            articles = Article.objects.all()
        serializer = ArticleListSerializer(
            articles, 
            many=True, 
            context={'request': request}
        )
        return Response(serializer.data)
    # if request.method == 'GET':
    #     articles = get_list_or_404(Article)
    #     serializer = ArticleListSerializer(articles, many=True, context={'request': request})
    #     return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        print(serializer.data)
        return Response(serializer.data)


@api_view(['POST', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def article_like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'POST':
        article.liked_users.add(request.user)
        return Response({'message':'liked'}, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        article.liked_users.remove(request.user)
        return Response({'message':'unliked'}, status=status.HTTP_204_NO_CONTENT)