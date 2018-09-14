from django.shortcuts import render
from datetime import date
# Create your views here.

def tasks(request):
    today = date.today()
    tasks = [{
        'Task' : 'Task {}'.format(i) ,
        'Created': today.strftime("%d/%m/%y"),
        'Due': today.replace(day = today.day + 2).strftime("%d/%m/%y"),
        'Owner': 'admin',
        'Mark': 'Done',
        'Complete': False} for i in range(1, 5)
    ]
    context = {'tasks':tasks }
    return render(request,'todo_list.html',context)

def completed_tasks(request):
    today = date.today()
    tasks = {
        'Task' : 'Task 0',
        'Created': today.strftime("%d/%m/%y"),
        'Due': today.replace(day = today.day + 2).strftime("%d/%m/%y"),
        'Owner': 'admin',
        'Mark': 'Not Done',
        'Complete': True
    }
    return render(request,'completed_todo_list.html',tasks)