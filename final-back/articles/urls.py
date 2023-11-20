from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list),  # 게시글 전체조회, 게시글 생성
    path('<int:article_pk>/', views.article_detail),    # 게시글 상세 조회, 수정, 삭제

    path('comments/', views.comment_list), # 댓글 전체 조회
    path('comments/<int:comment_pk>/', views.comment_detail), # 댓글 상세 조회, 수정, 삭제
    path('<int:article_pk>/comments/', views.comment_create), # 댓글 생성
]