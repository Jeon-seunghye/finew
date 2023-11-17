from django.urls import path
from . import views

urlpatterns = [
    path('deposit_save_data/', views.deposit_save_data),    # 예금 API 받아서 DB에 저장
    path('saving_save_data/', views.saving_save_data),    # 적금 API 받아서 DB에 저장
    path('exchange_rate_save_data/', views.exchange_rate_save_data),    # 환율정보 API 받아서 DB에 저장
    path('deposits/', views.deposit_list),  # 예금 전체 조회
    path('deposit/<int:deposit_pk>/', views.deposit_detail),    # 예금 상세정보
    path('savings/', views.saving_list),    # 적금 전체 조회
    path('saving/<int:saving_pk>/', views.saving_detail),   # 적금 상세정보
    path('exchange_rate/', views.exchange_rate),    # 환율 계산기
]
