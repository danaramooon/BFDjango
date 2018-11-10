from django.shortcuts import render,redirect
from .models import Task
from datetime import date, timedelta
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from .forms import TaskForm,UpdateTaskForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'Task'

    def get_queryset(self):
        return Task.objects.for_user(user= self.request.user)


class CompleteListView(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'Task'
    template_name = "main/completed_todo_list.html"
    queryset = Task.complete_obj.all()

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['name', 'due_on', 'owner', 'mark']
    success_url = reverse_lazy('todos')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class TaskDeleteView(LoginRequiredMixin,DeleteView):
    model = Task
    success_url = reverse_lazy('todos')

    def get_queryset(self):
        return Task.objects.for_user(user=self.request.user)

class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model = Task
    form_class = UpdateTaskForm
    success_url = reverse_lazy('todos')

    def get_queryset(self):
        return Task.objects.for_user(user= self.request.user)

def home(request):
    return render(request,'main/home.html')
