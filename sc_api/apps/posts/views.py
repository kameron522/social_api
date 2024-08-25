from django.shortcuts import render
from rest_framework.views import APIView
from .services import PostService
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsOwnerOrReadOnly
from . models import Post
from utils.DelImg import DelImg


class Index(APIView):
    def get(self, request):
        result = PostService.AllPosts()
        return result


class Store(APIView):
    permission_classes = [IsAuthenticated,]
    def post(self, request):
        result = PostService.CreatePost(self, request)
        return result
    
    
class Show(APIView):
    def get(self, request, pk):
        result = PostService.PostDetails(self, request, pk)
        return result
    

class Update(APIView):
    permission_classes = [IsOwnerOrReadOnly,]
    def patch(self, request, pk):
        post = Post.objects.get(id=pk)
        self.check_object_permissions(request, post)
        result = PostService.UpdatePost(self, request, post)
        return result

    
class Destroy(APIView):
    permission_classes = [IsOwnerOrReadOnly,]
    def delete(self, request, pk):
        post = Post.objects.get(id=pk)
        self.check_object_permissions(request, post)
        result = PostService.DeletePost(self, request, post)
        return result
    

class DelImg(APIView):
    permission_classes = [IsOwnerOrReadOnly,]
    def delete(self, request, pk):
        post = Post.objects.get(id=pk)
        self.check_object_permissions(request, post)
        return DelImg(post)