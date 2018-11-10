from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from api2.serializers import UserModelSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username,password=password)
    if user is None:
        return Response({'error':'Invalid Data'})

    token,created = Token.objects.get_or_create(user=user)
    return Response({'token':token.key})

@api_view(['POST'])
def register(request):
    serializer = UserModelSerializer(data = request.data)
    if serializer.is_valid():
        user = serializer.save()
    if user:

        token = Token.objects.create(user = user)
        json = serializer.data
        json['token'] = token.key
        return Response(json,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

