from django.db import models
from datetime import datetime,timedelta
from django import forms
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

# Create your models here.
class TaskManager(models.Manager):
    def for_user(self, user):
        return self.filter(owner=user)

class CompletedTaskManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(mark = True)

class Task(models.Model):
    name = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)
    due_on = models.DateTimeField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name="tasks",default=User,null=True)
    mark = models.BooleanField(default=False)
    objects = TaskManager()
    complete_obj = CompletedTaskManager()

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id':self.id,
            'name':self.name,
            'owner':self.owner.username if self.owner else None,
            'created_time':self.created_time,
            'due_on':self.due_on,
            'mark':self.mark
        }
