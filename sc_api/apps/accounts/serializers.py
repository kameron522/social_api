from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'] 
        )
        user.set_password(validated_data['password'])
        user.save()
        return user