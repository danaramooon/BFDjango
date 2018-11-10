from rest_framework import serializers
from main.models import Task
from django.contrib.auth.models import User
from datetime import datetime, timedelta


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    is_staff = serializers.BooleanField


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff')


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    created_time = serializers.DateTimeField()
    due_on = serializers.DateTimeField()
    owner = UserSerializer(read_only=True)
    mark = serializers.BooleanField()

    def create(self, validated_data):
        task = Task(**validated_data)
        task.owner = User.objects.get_by_natural_key(username='admin1')
        task.created_time = datetime.now()
        task.due_on = datetime.now() + timedelta(days=2)
        task.save()
        return task

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class TaskModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'created_time', 'due_on', 'owner', 'mark')














