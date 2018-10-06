from django.forms import ModelForm
from django import forms
from .models import User,Post,Comment

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author','content', 'date')

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('author','comment', 'date','posts')

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name', 'username','password','email')