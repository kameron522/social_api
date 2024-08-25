from django.db import models
from django.utils import timezone
from django.utils.timesince import timesince
from django.contrib.auth.models import User


class Message(models.Model):
    sender = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='received_messages')
    text = models.CharField(null=True, blank=True, max_length=1000)
    img = models.ImageField(null=True, blank=True, upload_to='imgs/messages/')
    modified = models.DateTimeField(default=timezone.now)
    
    @property
    def timesince(self):
        return timesince(self.modified)
    
    def __str__(self):
        return f'{self.text}'