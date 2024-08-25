from django.shortcuts import render
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from utils.permissions import IsOwnerOrReadOnly, IsMessageSenderOrReceiver
from rest_framework.views import APIView
from .services import MessageService
from . models import Message
from utils.DelImg import DelImg
from django.contrib.auth.models import User


class Index(APIView):
    permission_classes = [IsAdminUser,]
    def get(self, request):
        result = MessageService.AllMessages()
        return result

class Store(APIView):
    permission_classes = [IsAuthenticated,]
    def post(self, request, receiver_pk):
        result = MessageService.CreateMessage(self, request, receiver_pk)
        return result

class Show(APIView):
    permission_classes = [IsMessageSenderOrReceiver,]
    def get(self, request, pk):
        msg = Message.objects.get(id=pk)
        self.check_object_permissions(request, msg)
        result = MessageService.ShowMessage(self, request, msg)
        return result
        
class Update(APIView):
    permission_classes = [IsOwnerOrReadOnly,]
    def patch(self, request, pk):
        msg = Message.objects.get(id=pk)
        self.check_object_permissions(request, msg)
        result = MessageService.UpdateMessage(self, request, msg)
        return result
        
class Destroy(APIView):
    permission_classes = [IsOwnerOrReadOnly,]
    def delete(self, request, pk):
        msg = Message.objects.get(id=pk)
        self.check_object_permissions(request, msg)
        result = MessageService.DeleteMessage(self, request, msg)
        return result
    
class DelImg(APIView):
    permission_classes = [IsOwnerOrReadOnly,]
    def delete(self, request, pk):
        msg = Message.objects.get(id=pk)
        self.check_object_permissions(request, msg)
        return DelImg(msg)
    
    
class UserMessages(APIView):
    permission_classes = [IsOwnerOrReadOnly,]
    def get(self, request):
        result = MessageService.AllUserMessages(self, request)
        return result