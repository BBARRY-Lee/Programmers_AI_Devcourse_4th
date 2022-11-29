from django.contrib import admin
from .models import Coffee
# Register your models here.
# 모델을 어드민과 연동하면, admin 페이지에서 관리가능

admin.site.register(Coffee)
