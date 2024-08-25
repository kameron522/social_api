from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Follow
from rest_framework.views import APIView
from .services import FollowService
from rest_framework.response import Response
from rest_framework import status
from utils.permissions import IsOwnerOrReadOnly


class Store(APIView):
    permission_classes = [IsAuthenticated,]
    def post(self, request, receiver_pk):
        receiver = User.objects.get(id=receiver_pk)
        if IsFollowing(request.user, receiver):
            return Response({'error' : 'Followed already'}, status=status.HTTP_400_BAD_REQUEST)
        result = FollowService.FollowUser(self, request, receiver)
        return result


class Destroy(APIView):
    permission_classes = [IsOwnerOrReadOnly,]
    def delete(self, request, receiver_pk):
        receiver = User.objects.get(id=receiver_pk)
        self.check_object_permissions(request, receiver)
        result = FollowService.UnfollowUser(self, request, receiver)
        return result
        

def IsFollowing(sender, receiver):
    follow_relation = Follow.objects.filter(sender=sender, receiver=receiver)
    if follow_relation:
        return True
    return False