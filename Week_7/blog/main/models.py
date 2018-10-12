from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(default=datetime.now())
    content = models.TextField()

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    date = models.DateTimeField(default=datetime.now())
    comment = models.CharField(max_length=255)
