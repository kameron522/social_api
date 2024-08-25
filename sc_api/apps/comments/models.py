from django.db import models
from django.contrib.auth.models import User
from apps.posts.models import Post
from django.utils import timezone
from django.utils.timesince import timesince


class Comment(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE, related_name='comments')
    body = models.CharField(max_length=255)
    modified = models.DateTimeField(default=timezone.now)
    
    @property
    def timesince(self):
        return timesince(self.modified)
    
    def __str__(self):
        return f'{self.body}'