"""webproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from homepage.views import index, coffee_view # homepage directory 안의 views.py의 index 함수 호출

urlpatterns = [
    path('', index), # 127.0.0.1/ # 빈경로, 루트경로가 들어왔을 때 index 실행하라는 패턴
    path('coffee/', coffee_view), # 127.0.0.1/coffee/
    path('admin/', admin.site.urls), # 127.0.0.1/adimin/
]
