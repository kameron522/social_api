from utils.ServiceWrapper import ServiceWrapper
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from apps.messages.models import Message
from apps.messages.serializers import MessageSerializer
from .password_validation import password_validation
from rest_framework.response import Response


class UserService():
    
    
    def AllUsers():
        def action():
            users = User.objects.all()
            srz_data = UserSerializer(instance=users, many=True)
            return srz_data.data, 200
        return ServiceWrapper(action)
    
    
    def CreateUser(self, request):
        if not password_validation(self, request):
            return Response({'error' : 'passwords must match'}, status=422)
        def action():
            srz_data = UserSerializer(data=request.data)
            if srz_data.is_valid():
                srz_data.save()
                return srz_data.data, 200
            return srz_data.errors, 422
        return ServiceWrapper(action)
    
    
    def UserProfile(self, request, user):
        def action():
            srz_data = UserSerializer(instance=user)
            return srz_data.data, 200
        return ServiceWrapper(action)
    
    
    def UpdateUser(self, request, user):
        def action():
            srz_data = UserSerializer(instance=user, data=request.data, partial=True)
            if srz_data.is_valid():
                srz_data.save()
                return srz_data.data, 200
            return srz_data.errors, 422
        return ServiceWrapper(action)
    
    
    def DeleteUser(self, request, user):
        def action():
            user.delete()
            return "User Deleted!", 200
        return ServiceWrapper(action)
    
    
    def DeleteToken(self, request):
        def action():
            token = Token.objects.get(user=request.user)
            token.delete()
            return "Logged out!", 200
        return ServiceWrapper(action)
