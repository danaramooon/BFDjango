from django.shortcuts import render, get_object_or_404
from .models import Task, Owner
from datetime import date, timedelta
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def todos(request):
    tasks = Task.objects.all()
    context = {
        'Task': tasks
    }
    return render(request, 'todos.html', context)


@csrf_exempt
def completed_todos(request):
    tasks = [i for i in Task.objects.all() if i.mark]
    context = {
        'Task': tasks
    }
    return render(request, 'completed_todo_list.html', context)


@csrf_exempt
def todo_filter(request,param):
    task = Task.objects.order_by(param)
    context = {
        'Task': task
    }
    return render(request, "todos.html", context)
@csrf_exempt
def completed_todo_filter(request,param):
    task = Task.objects.filter(mark = True).order_by(param)
    context = {
        'Task': task
    }
    return render(request, "completed_todo_list.html", context)
