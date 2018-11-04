from django.forms import ModelForm
from django import forms
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'due_on', 'owner', 'mark')

class UpdateTaskForm(ModelForm):
    class Meta:
        model = Task
        fields=('name',)
