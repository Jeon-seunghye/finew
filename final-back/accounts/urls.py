from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.user_detail),  # 유저 정보 상세 조회, 수정
    path('financial_product/deposit/<int:deposit_id>/', views.financial_products_deposit), # 예금 상품 가입
    path('financial_product/saving/<int:saving_id>/', views.financial_products_saving), # 적금 상품 가입
    path('financial_product/', views.financial_product_list),   # 유저별 상품가입목록 가져오기
]