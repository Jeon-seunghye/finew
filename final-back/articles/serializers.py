from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        # 댓글도 나오게 갖고오자 직렬화 상속

class CommentSerializer(serializers.ModelSerializer):
    class Comment:
        model = Comment
        fields = '__all__'