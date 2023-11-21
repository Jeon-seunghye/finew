from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.user_detail),  # 유저 상세 조회, 수정
    path('financial_product/', views.financial_product) # 금융상품 가입, 가입취소
]