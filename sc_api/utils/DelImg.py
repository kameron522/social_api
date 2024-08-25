from django.contrib.auth.models import User
from apps.posts.models import Post
from rest_framework.response import Response
from rest_framework import status


def DelImg(obj):
    try:    
        if obj and obj.img:
            obj.img.delete()
            obj.img = None
            obj.save()
        
    except Exception as ex:
        return Response({'error' : str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    finally:
        return obj