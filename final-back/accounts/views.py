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
@api_view(['GET'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def financial_products_saving(request, saving_id):
    product = SavingOption.objects.get(pk=saving_id)
    if product in request.user.saving_options.all():
        request.user.saving_options.remove(product)
        return Response({'message':'remove okay'})
    else:
        request.user.saving_options.add(product)
        return Response({'message':'add okay'})


# 유저별 상품가입목록 가져오기
@api_view(['GET'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def financial_product_list(request):
    products = FinancialProduct.objects.filter(user_id=request.user.pk)
    if request.method == 'GET':
        serializer = FinancialProductSerializer(products, many=True)
        return Response(serializer.data)
    
# 유저 선호 조회/생성/수정
@api_view(['GET', 'POST', 'PUT'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def my_preference(request):
    # 조회
    if request.method == 'GET':
        mypreference = MyPreference.objects.filter(user_id=request.user.pk)
        serializer = MyPreferenceSerializer(mypreference, data=request.data)
        return Response(serializer.data)
    # 생성
    elif request.method == 'POST':
        serializer = MyPreferenceSerializer(data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # 수정
    elif request.method == 'PUT':
        mypreference = MyPreference.objects.get(user_id=request.user.pk, partial=True)
        serializer = MyPreferenceSerializer(mypreference, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)