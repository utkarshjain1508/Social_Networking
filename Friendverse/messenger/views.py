from django.shortcuts import render
from django.utils.safestring import mark_safe
from home.models import CustomUser, Connection
from . import models
import json

def index(request, sender_id):
    custom_user = CustomUser.objects.get(id=sender_id)
    connections = Connection.objects.filter(user=custom_user, status='confirmed')
    # print(json.dumps(vars(custom_user)))
    var = vars(custom_user)
    
    return render(request, 'messenger/index.html', {
        'sender_id_json': sender_id,
        'connections': connections,
        'profile' : var
    })
def room(request):
    print('madarchod')
