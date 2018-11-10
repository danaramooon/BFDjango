from rest_framework import generics
from api2.serializers import TaskModelSerializer
from main.models import Task
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class TaskGenericListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Task.objects.for_user( self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)
