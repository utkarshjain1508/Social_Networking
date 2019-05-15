# messenger/urls.py
from django.urls import path

from . import views

app_name = 'messenger'

urlpatterns = [
    path('<slug:sender_id>', views.base, name='base'),
    path('<slug:sender_id>/<slug:receiver_id>', views.room, name='room'),
]
