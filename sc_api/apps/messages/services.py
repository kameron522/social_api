from .models import Message
from .serializers import MessageSerializer
from utils.ServiceWrapper import ServiceWrapper
from .msg_validation import msg_validation
from django.contrib.auth.models import User


class MessageService():
    
    def AllMessages():
        def action():
            messages = Message.objects.all().order_by('-modified')
            srz_data = MessageSerializer(instance=messages, many=True)
            return srz_data.data, 200
        return ServiceWrapper(action)
    
    
    def CreateMessage(self, request, receiver_pk):
        def action():
            receiver = User.objects.get(id=receiver_pk)
            if not msg_validation(self, request):
                return "fill at least one field", 422
            srz_data = MessageSerializer(data=request.data)
            if srz_data.is_valid():
                srz_data.save(sender=request.user, receiver=receiver)
                return "Message sent!", 200
            return srz_data.errors, 422
        return ServiceWrapper(action)
    
    
    def ShowMessage(self, request, msg):
        def action():
            return {'sender' : str(msg.sender), 'text' : str(msg.text), 'received' : msg.timesince + " ago"}, 200
        return ServiceWrapper(action)
    
    
    def UpdateMessage(self, request, msg):
        def action():
            srz_data = MessageSerializer(instance=msg, data=request.data, partial=True)
            if srz_data.is_valid():
                srz_data.save()
                return srz_data.data, 200
            return srz_data.errros, 422
        return ServiceWrapper(action)
    
    
    def DeleteMessage(self, request, msg):
        def action():
            msg.img.delete()
            msg.delete()
            return "Message deleted", 200
        return ServiceWrapper(action)
    
    
    def AllUserMessages(self, request):
        def action():
            user_messages = Message.objects.filter(receiver=request.user) | Message.objects.filter(sender=request.user)
            srz_data = MessageSerializer(instance=user_messages, many=True)
            return srz_data.data, 200
        return ServiceWrapper(action) 
            
    
    