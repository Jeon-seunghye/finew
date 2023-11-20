from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import render
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment

# 인증이 필요한 요소들에게 데코레이터 등록 (401)
## @authentication_classes([TokenAuthentication, BasicAuthentication])

# 권한 정책 설정 (403)
## @permission_classes([IsAuthenticated])


# 게시글
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def article_list(request):
    # 게시글 전체 조회
    if request.method == 'GET':
        article = Article.objects.all()
        serializers = ArticleListSerializer(article, many=True)
        return Response(serializers.data)
    # 게시글 생성
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 게시글 상세정보
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    # 게시글 조회
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    # 게시글 수정
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    # 게시글 삭제
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 댓글 생성
@authentication_classes([TokenAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 댓글 삭제
@authentication_classes([TokenAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def comment_delete(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)