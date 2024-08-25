from rest_framework.permissions import BasePermission, SAFE_METHODS 
from django.contrib.auth.models import User


class IsOwnerOrReadOnly(BasePermission):
    
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        if type(obj) == User:
            if request.method in SAFE_METHODS:
                return True
            return request.user == obj
        
        if request.method in SAFE_METHODS:
            return True
        return request.user == obj.user
    
    
class IsMessageSenderOrReceiver(BasePermission):
    
    def has_permission(sekf, request, view):
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, message):
        return request.user == message.sender or request.user == message.receiver