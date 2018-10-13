from django import forms
from .models import Post,Comment

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=('title','content')
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=('title','date','content')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=('user','date','comment')

class UpdateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
