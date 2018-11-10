from rest_framework import status
from main.models import Task
from api2.serializers import TaskModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class TaskListView(APIView):
    def get(self,request):
        task = Task.objects.all()
        serializer = TaskModelSerializer(task,many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = TaskModelSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class TaskDetailView(APIView):
    def get_object(self,pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,pk):
        task = self.get_object(pk=pk)
        serializer = TaskModelSerializer(task)
        return Response(serializer.data)

    def put(self,request,pk):
        task = self.get_object(pk=pk)
        serializer = TaskModelSerializer(instance =task,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        task = self.get_object(pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

