from .models import Comment
from .serializers import CommentSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from utils.permissions import IsOwnerOrReadOnly
from apps.posts.models import Post
from utils.ServiceWrapper import ServiceWrapper


class CommentService():
    
    
    def AllComments():
        def action():
            comments = Comment.objects.all().order_by('-modified')
            srz_data = CommentSerializer(instance=comments, many=True)
            return srz_data.data, 200
        return ServiceWrapper(action)
    
    def CreateComment(self, request, post):
        def action():
            srz_data = CommentSerializer(data=request.data)
            if srz_data.is_valid():
                srz_data.save(
                    user=request.user,
                    post=post,
                )
                return srz_data.data, 200
            return srz_data.errors, 422
        return ServiceWrapper(action)
    
    
    def CommentDetails(self, request, pk):
        def action():
            comment = Comment.objects.get(id=pk)
            return comment, 200
        return ServiceWrapper(action)
    
    
    def UpdateComment(self, request, comment):
        def action():
            srz_data = CommentSerializer(instance=comment, data=request.data, partial=True)
            if srz_data.is_valid():
                srz_data.save()
                return srz_data.data, 200
            return srz_data.errors, 422
        return ServiceWrapper(action)
    
    
    def DeleteComment(self, request, comment):
        def action():
            comment.delete()
            return "comment deleted", 422
        return ServiceWrapper(action)