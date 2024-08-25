from utils.ServiceWrapper import ServiceWrapper
from .serializers import PostSerializer
from .models import Post
from utils.UuidGegerator import Uuid
from rest_framework.response import Response


class PostService():
    
    
    def AllPosts():
        def action():
            posts = Post.objects.all().order_by('-modified')
            srz_data = PostSerializer(instance=posts, many=True)
            return srz_data.data, 200
        return ServiceWrapper(action)
        
    
    def CreatePost(self, request):
        def action():
            srz_data = PostSerializer(data=request.data)
            if srz_data.is_valid():
                srz_data.save(
                    uuid=Uuid(Post.objects.all()),
                    user=request.user,
                )
                return srz_data.data, 200
            return srz_data.errors, 422
        return ServiceWrapper(action)
    
    
    def PostDetails(self, request, pk):
        def action():
            post = Post.objects.get(id=pk)
            srz_data = PostSerializer(instance=post)
            return srz_data.data, 200
        return ServiceWrapper(action)

        
    def UpdatePost(self, request, post):
        def action():
            if post.img:
                post.img.delete()
            srz_data = PostSerializer(instance=post, data=request.data, partial=True)
            if srz_data.is_valid():
                srz_data.save()
                return srz_data.data, 200
            return srz_data.errors, 422
        return ServiceWrapper(action)
    
    
    def DeletePost(self, request, post):
        def action():
            post.img.delete()
            post.delete()
            return "Object Deleted!", 200
        return ServiceWrapper(action)
            