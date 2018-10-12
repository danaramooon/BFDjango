from django.db import models
from datetime import datetime,timedelta
from django import forms
from django.views.decorators.csrf import csrf_exempt

# Create your models here.

class Owner(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=100)
    created_time = models.DateTimeField(default=datetime.now())
    due_on = models.DateTimeField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE,related_name="tasks")
    mark = models.BooleanField(default=False)

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.
