from rest_framework import serializers
from .models import Article, Comment
from django.contrib.auth import get_user_model


    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)


class ArticleListSerializer(serializers.ModelSerializer):
    class UserNameSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('username',)
    user = UserNameSerializer(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)  # 단일 게시글 조회 시 해당 게시글에 작성된 댓글 목록 데이터
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)    # 댓글 개수
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)
