from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .serializers import AuthSerializer

@api_view(['POST'])
def register(request):
    serializer = AuthSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        return Response({ 'user': serializer.data })
    return Response(serializer.error, status=status.HTTP_200_OK)

@api_view(['POST'])
def login(request):
    pass

@api_view(['GET'])
def logout(request):
    pass