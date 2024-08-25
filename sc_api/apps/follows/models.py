from django.db import models
from django.contrib.auth.models import User

class Follow(models.Model):
    sender = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='follows')  # this user is the person who followes someone
    receiver = models.ForeignKey(User, null=True,  on_delete=models.CASCADE, related_name='followed_by')  # this is the person who is bieng followed
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.sender} followes {self.receiver}'
