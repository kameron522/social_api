from utils.ServiceWrapper import ServiceWrapper
from django.contrib.auth.models import User
from .models import Follow


class FollowService():
    
    def FollowUser(self, request, receiver):
        def action():
            if request.user == receiver:
                return 'you can not follow your self', 400
            Follow.objects.create(
                sender=request.user,
                receiver=receiver
            )
            return f'you are now following {receiver}', 200
        return ServiceWrapper(action)
    
    
    def UnfollowUser(self, request, receiver):
        def action():
            follow_relation = Follow.objects.filter(receiver=receiver)
            follow_relation.delete()
            return "you unfollowed this person", 200
        return ServiceWrapper(action)
            