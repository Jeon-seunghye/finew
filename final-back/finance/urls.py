from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('banks/', include('banks.urls')),
    path('accounts/', include('dj_rest_auth.urls')),
]
