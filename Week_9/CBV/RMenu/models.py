from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class Restau(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    telephone = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="restaurants")