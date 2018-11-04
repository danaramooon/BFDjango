from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

class MyPostManager(models.Manager):
    def my_post(self,user):
        return self.filter(owner=user)

class MyIdManager(models.Manager):
    def my_post(self,id):
        return self.filter(id=id)

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(default = datetime.now())
    owner = models.ForeignKey(User,on_delete=models.CASCADE,default=User)
    myPost = MyPostManager()
    object = MyIdManager()

class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(default=datetime.now())
    owner = models.ForeignKey(User,on_delete=models.CASCADE,default= User)
    myPost = MyPostManager()