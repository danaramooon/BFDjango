from django.db import models
from django.views.decorators.csrf import csrf_exempt

# Create your models here.

class Owner(models.Model):
    name = models.CharField(max_length=100)


class Task(models.Model):
    name = models.CharField(max_length=100)
    created_time = models.CharField(max_length=100)
    due_on = models.CharField(max_length=100)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    mark = models.BooleanField(default=False)

    def __str__(self):
        return self.name
