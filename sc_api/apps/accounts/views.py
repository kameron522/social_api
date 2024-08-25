from django.shortcuts import render
from .services import UserService
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from utils.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from apps.messages.models import Message


class Index(APIView):
    permission_classes = [IsAdminUser,]
    def get(self, request):
        result = UserService.AllUsers()
        return result


class Store(APIView):
    def post(self, request):
        result = UserService.CreateUser(self, request)
        return result


class Show(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request, pk):
        user = User.objects.get(id=pk)
        result = UserService.UserProfile(self, request, user)
        return result
    
    
class Update(APIView):
    permission_classes = [IsOwnerOrReadOnly,]
    def patch(self, request, pk):
        user = User.objects.get(id=pk)
        self.check_object_permissions(request, user)
        result = UserService.UpdateUser(self, request, user)
        return result
    
    
class Destroy(APIView):
    permission_classes = [IsOwnerOrReadOnly,]
    def delete(self, request, pk):
        user = User.objects.get(id=pk)
        self.check_object_permissions(request, user)
        result = UserService.DeleteUser(self, request, user)
        return result
    
    
class DeleteToken(APIView):
    def delete(self, request):
        result = UserService.DeleteToken(self, request)
        return result
    
        