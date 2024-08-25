from django.db import models
from django.contrib.auth.models import User
from apps.posts.models import Post


class Like(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE, related_name='likes')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user}'