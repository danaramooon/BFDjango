from django.forms import ModelForm
from django import forms
from .models import Task,Owner

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'created_time','due_on', 'owner', 'mark')
