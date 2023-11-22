from rest_framework import serializers
from allauth.account import app_settings as allauth_settings
from allauth.utils import get_username_max_length
from allauth.account.adapter import get_adapter
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from .models import *



class CustomRegisterSerializer(RegisterSerializer):
    # 추가할 필드들을 정의합니다.
    nickname = serializers.CharField(required=False,allow_blank=True,max_length=255,)
    age = serializers.IntegerField(required=False)
    money = serializers.IntegerField(required=False)
    salary = serializers.IntegerField(required=False)
    email = serializers.EmailField(required=False)
    financial_products = serializers.ListField(child=serializers.IntegerField(), required=False)

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username',''),
            'password1': self.validated_data.get('password1',''),
            'nickname': self.validated_data.get('nickname',''),
            'age': self.validated_data.get('age',''),
            'money': self.validated_data.get('money',''),
            'salary': self.validated_data.get('salary',''),
            'email': self.validated_data.get('email',''),
            'financial_products': self.validated_data.get('financial_products',''),
            }
    
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        return user
    
    def update(self, instance, validated_data):
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.age = validated_data.get('age', instance.age)
        instance.money = validated_data.get('money', instance.money)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.email = validated_data.get('email', instance.email)
        instance.financial_product = validated_data.get('financial_product', instance.financial_product)
        
        instance.save()
        return instance
    
class CustomUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'


class FinancialProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialProduct
        fields = '__all__'