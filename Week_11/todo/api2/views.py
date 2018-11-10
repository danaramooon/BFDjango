from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .serializers import TaskSerializer,TaskModelSerializer
from main.models import Task
from django.http import JsonResponse
import json

@csrf_exempt
def task_list(request):
    if request.method == "GET":
        task = Task.objects.all()
        serializer = TaskSerializer(task,many = True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == "POST":
        data = json.loads(request.body)
        serializer = TaskModelSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error':"invalid data"})

@csrf_exempt
def task_detail(request,pk):
    try:
        task = Task.objects.get(id=pk)
    except Exception as e:
        return JsonResponse({'Error':str(e)},status = 404)

    if request.method == "GET":
        serializer = TaskModelSerializer(task)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        data = json.loads(request.body)
        serializer = TaskSerializer(instance=task,data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error':'invalid data'})
    elif request.method == "DELETE":
        task.delete()
        return JsonResponse({'deleted':True})

