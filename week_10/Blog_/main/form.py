from .models import Post,Comment
from django.forms import ModelForm
class PostUpdateForm(ModelForm):
    class Meta:
        model = Post
        fields = ('text',)