from django.shortcuts import render,redirect
from .models import Task, Owner
from datetime import date, timedelta
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from .forms import TaskForm
from django.contrib.auth.decorators import login_required

@csrf_exempt
def todos(request):
    tasks = Task.objects.all()
    context = {
        'Task': tasks
    }
    return render(request, 'todos.html', context)


@csrf_exempt
def completed_todos(request):
    tasks = Task.objects.filter(mark=True)
    context = {
        'Task': tasks
    }
    return render(request, 'completed_todo_list.html', context)


@login_required
def todo_filter(request,param):
    task = Task.objects.order_by(param)
    context = {
        'Task': task
    }
    return render(request, "todos.html", context)
@login_required
def completed_todo_filter(request,param):
    try:
        task = Task.objects.filter(mark=True).order_by(param)
    except Task.DoesNotExist:
        raise Http404("Author not found")
    context = {
        'Task': task
    }
    return render(request, "completed_todo_list.html", context)

@login_required
def add_new(request):
        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('todos')
        else:
            form = TaskForm()
        context = {
            'form': form
        }
        return render(request, 'add_new_task.html', context)


@login_required
def change_button(request,id):
    try:
        task = Task.objects.get(pk = id)
    except Task.DoesNotExist:
        raise Http404("Task not found")
    if task.mark == False:
        task.mark = True
    else:
        task.mark = False
    task.save()
    task = Task.objects.all()
    context = {
        'Task':task
    }
    return render(request,"todos.html",context)

@login_required
def delete(request,id):

    task = Task.objects.exclude(pk = id)
    context = {
        'Task':task
    }
    return render(request,"todos.html",context)

@login_required
def owner_detail(request,id):
    try:
        owner = Owner.objects.get(id=id)
    except Task.DoesNotExist:
        raise Http404("Owner not found")
    context ={
        'owner':owner,
        'tasks':owner.tasks.all()
    }
    return render(request,"owner_detail.html",context)

def home(request):
    return render(request,'home.html')
