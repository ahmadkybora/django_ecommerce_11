from rest_framework import serializers
from .models import User
from django.core.validators import MinLengthValidator

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

        # username = serializers.CharField(max_length=2)

    # def create(self, instance, validate_data):
    #     instance.username = validate_data.get('username', instance.username)
    #     instance.password = validate_data.get('password', instance.password)
    #     instance.email = validate_data.get('email', instance.email)
    #     instance.save()
    #     return instance

    def validate_username(self, value):
        if len(value) <= 3:
            raise serializers.ValidationError("Username must not be less than 3 characters.")
    
        if len(value) >= 32:
            raise serializers.ValidationError("Username should not be more than 32 characters.")
        
        return value
    
    def validate_password(self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("Password must not be less than 2 characters.")
        
        return value