from django.shortcuts import render
from rest_framework.views import APIView
from apps.posts.models import Post
from .services import LikeService
from .models import Like
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from utils.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework import status


class Store(APIView):
    permission_classes = [IsAuthenticated,]
    def post(self, request, post_pk):
        if HasLiked(request.user, post_pk):
            return Response({'error' : 'you have already liked this post!'}, status=status.HTTP_400_BAD_REQUEST)
        post = Post.objects.get(id=post_pk)
        result = LikeService.AddLike(self, request, post)
        return result
    
class Destroy(APIView):
    permission_classes = [IsOwnerOrReadOnly,]
    def delete(self, request, like_pk):
        like = Like.objects.get(id=like_pk)
        self.check_object_permissions(request, like)
        result = LikeService.RemoveLike(self, request, like)
        return result

def HasLiked(user,post_pk):
    post = Post.objects.get(id=post_pk)
    like = Like.objects.filter(post=post, user=user)
    if like:
        return True
    return False