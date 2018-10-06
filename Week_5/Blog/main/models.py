from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    email = models.EmailField()

class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField(editable=True)
    date = models.DateField(auto_now=False, editable=True)


class Comment(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="comments")
    comment = models.CharField(max_length=255)
    date = models.DateField(auto_now=False, editable=True)
    posts = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")








# Create your models here.
