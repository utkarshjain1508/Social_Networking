from django.shortcuts import render
from django.utils.safestring import mark_safe
from home.models import CustomUser, Connection
from . import models
import json

def base(request, sender_id):
    custom_user = CustomUser.objects.get(id=sender_id)
    connections = Connection.objects.filter(user=custom_user, status='confirmed')
    return render(request, 'messenger/base.html', {
        'sender_id_json': sender_id,
        'connections': connections
    })

def room(request, sender_id, receiver_id):
    custom_user = CustomUser.objects.get(id=sender_id)
    connections = Connection.objects.filter(user=custom_user, status='confirmed')
    return render(request, 'messenger/room.html', {
        # 'sender_id_json': mark_safe(json.dumps(sender_id)),
        # 'receiver_id_json': mark_safe(json.dumps(receiver_id)),
        'sender_id_json': sender_id,
        'receiver_id_json': receiver_id,
        'connections': connections
    })

# Create your views here.
