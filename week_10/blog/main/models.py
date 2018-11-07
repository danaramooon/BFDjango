from django.db import models
from django.contrib.auth.models import User

class PostOwnerManager(models.Manager):
    def for_user(self,user):
        return self.filter(created_by=user)

class Post(models.Model):
    title = models.CharField(max_length=25)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name="posts")
    my_post = PostOwnerManager()
    objects = models.Manager()

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments",null=True)

