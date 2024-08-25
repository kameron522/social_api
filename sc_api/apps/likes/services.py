from utils.ServiceWrapper import ServiceWrapper
from apps.posts.models import Post
from .models import Like

class LikeService():
    def AddLike(self, request, post):
        def action():
            like = Like.objects.filter(user=request.user, post=post)
            if like:
                return "You have already liked this post!", 400
            
            Like.objects.create(
                user=request.user,
                post=post
            )
            return "Like added", 200
        return ServiceWrapper(action)
    
    def RemoveLike(self, request, like):
        def action():
            like.delete()
            return "Liked removed!", 200
        return ServiceWrapper(action)