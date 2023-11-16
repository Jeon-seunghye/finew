from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list),  # 게시글 전체조회, C
    path('<int:article_pk>/', views.article_detail),    # 게시글 detail R U D
    path('<int:article_pk>/comment/create/', views.comment_create), # 댓글 C
    path('comments/<int:comment_pk>/', views.comment_delete),   # 댓글 D
]