from django.db import models


# Create your models here. # class 단위로 모델 생성
class Coffee(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(default = "", max_length = 30) # null = False -> 반드시 값이 있어야 함
    price = models.IntegerField(default = 0)
    is_ice = models.BooleanField(default = False)