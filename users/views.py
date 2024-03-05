from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
# from django.shortcuts import get_object_or_404
# from django.contrib.auth.models import User
from .models import User
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        return Response({ 'user': serializer.data })
    return Response(serializer.error, status=status.HTTP_200_OK)

@api_view(['POST'])
def login(request):
    user = authenticate(username=request.data['username'], password=request.data['password'])
    if user:
        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(user)
        return Response({ 'token': token.key, 'user': serializer.data })
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    # user = get_object_or_404(User, username=request.data['username'])
    # if not user.check_password(request.data['password']):
    #     return Response("user not found", status=status.HTTP_404_NOT_FOUND)
    # token, created = Token.objects.get_or_create(user=user)
    # serializer = UserSerializer(user)
    # return Response({'token': token.key, 'user': serializer.data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    if request.method == 'POST':
        try:
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)