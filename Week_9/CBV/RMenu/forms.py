from django.forms import ModelForm
from .models import Restau
from django import forms

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restau
        fields = ('name','number','telephone','city','user')