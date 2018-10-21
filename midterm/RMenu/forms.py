from django.forms import ModelForm
from .models import Restau,Dish,RestaurantReview,DishReview
from django import forms

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restau
        fields = ('name','number','telephone','city','user')

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ('name','description','price','user','restaurant')

class ResRevForm(forms.ModelForm):
    class Meta:
        model = RestaurantReview
        fields = ('restaurant','rating','comment','date')

class DishRevForm(forms.ModelForm):
    class Meta:
        model = DishReview
        fields = ('dish','rating','comment','date')