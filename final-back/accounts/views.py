from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
# from rest_framework.authentication import TokenAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import render
from .serializers import *
from .models import *


@api_view(['GET', 'PUT'])
def user_detail(request):
    user = User.objects.get(pk=request.user.pk)
    # 유저 정보 조회
    if request.method == 'GET':
        serializer = CustomRegisterSerializer(user)
        return Response(serializer.data)
    # 유저 정보 수정
    elif request.method == 'PUT':
        serializer = CustomRegisterSerializer(user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.update(user, serializer.validated_data)
            return Response(serializer.data)

# financial product 생성, 삭제
@api_view(['PUT', 'DELETE'])
def financial_product(request):
    pass