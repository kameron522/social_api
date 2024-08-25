from django.shortcuts import render
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from utils.permissions import IsOwnerOrReadOnly
from apps.posts.models import Post
from utils.ServiceWrapper import ServiceWrapper
from rest_framework.views import APIView
from .services import CommentService

class Index(APIView):
    def get(self, request):
        result = CommentService.AllComments()
        return result

class Store(APIView):
    permission_classes = [IsAuthenticated,]
    def post(self, request, post_pk):
        post = Post.objects.get(id=post_pk)
        result = CommentService.CreateComment(self, request, post)
        return result
    
class Update(APIView):
    permission_classes = [IsOwnerOrReadOnly,]
    def patch(self, request, comment_pk):
        comment = Comment.objects.get(id=comment_pk)
        self.check_object_permissions(request, comment)
        result = CommentService.UpdateComment(self, request, comment)
        return result
    
class Destroy(APIView):
    permission_classes = [IsOwnerOrReadOnly,]
    def delete(self, request, comment_pk):
        comment = Comment.objects.get(id=comment_pk)
        self.check_object_permissions(request, comment)
        result = CommentService.DeleteComment(self, request, comment)
        return result
        