from django.db import models
from django.contrib.auth.models import User
from django.utils.timesince import timesince
from django.utils import timezone


class Post(models.Model):
    uuid = models.BigIntegerField(null=True, unique=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='posts')
    caption = models.CharField(max_length=1000)
    img = models.ImageField(null=True, blank=True, upload_to='imgs/posts/')
    modified = models.DateTimeField(default=timezone.now)
    
    @property
    def timesince(self):
        return timesince(self.modified)
    
    def __str__(self):
        return f'{self.user} - {self.caption[:10]} - {self.timesince}'
    
