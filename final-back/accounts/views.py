from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import render
from .serializers import *
from .models import *
from django.contrib.auth.decorators import login_required


@api_view(['GET', 'PUT'])
def user_detail(request):
    user = User.objects.get(pk=request.user.pk)
    # 유저 정보 조회
    if request.method == 'GET':
        serializer = CustomRegisterSerializer(user)
        return Response(serializer.data)
    # 유저 정보 수정
    elif request.method == 'PUT':
        serializer = CustomUserUpdateSerializer(user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.update(user, serializer.validated_data)
            return Response(serializer.data)

# 예금 상품 가입
@api_view(['GET'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def financial_products_deposit(request, deposit_id):
    product = DepositOption.objects.get(pk=deposit_id)
    if product in request.user.deposit_options.all():
        request.user.deposit_options.remove(product)
        return Response({'message':'remove okay'})
    else:
        request.user.deposit_options.add(product)
        return Response({'message':'add okay'})



# 적금 상품 가입
def financial_products_saving(request, saving_id):
    pass