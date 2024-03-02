from rest_framework import serializers
from django.contrib.auth.models import User

class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['username', 'password', 'email']
