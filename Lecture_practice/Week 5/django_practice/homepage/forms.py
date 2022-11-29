from django import forms
from .models import Coffee # Model 호출

class CoffeeForm(forms.ModelForm): # Modelform을 상속받는 Coffeeform 생성
    class Meta:
        model = Coffee
        fields = ('name', 'price', 'is_ice')