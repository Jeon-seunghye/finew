from rest_framework import serializers
from .models import Article, Comment
from django.contrib.auth import get_user_model


class CommentSerializer(serializers.ModelSerializer):
    class Comment:
        model = Comment
        fields = '__all__'


class ArticleListSerializer(serializers.ModelSerializer):
    # class CommentSetSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = Comment
    #         fields = ('content')
    # comment = CommentSetSerializer(read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)

    class UserNameSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('username',)
    user = UserNameSerializer(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)
