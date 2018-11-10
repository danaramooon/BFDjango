from django.views.decorators.csrf import csrf_exempt
from main.models import Task
from django.contrib.auth.models import User
from django.http import JsonResponse
import json

@csrf_exempt
def task_list(request):
    if request.method == "GET":
        tasks = Task.objects.all()
        tasks = [t.to_json() for t in tasks]
        return JsonResponse(tasks,safe=False)
    elif request.method== "POST":
        data = json.loads(request.body)
        task = Task(
             name=data['name'],
             due_on=data['due_on'],
             owner = User.objects.first(),
             mark = data['mark']
        )
        task.save()
        return JsonResponse(task.to_json())

@csrf_exempt
def task_detail(request,pk):
    try:
        task = Task.objects.get(id = pk)
    except Exception as e:
        return JsonResponse({'error':str(e)},status=404)

    if request.method == "GET":
        return JsonResponse(task.to_json())
    elif request.method == "PUT":
        data = json.loads(request.body)
        task.name = data.get('name',task.name)
        task.save() # SAVE dont forget
        return JsonResponse(task.to_json())
    elif request.method == "DELETE":
        task.delete
        return JsonResponse({'deleted':True},status = 204)




