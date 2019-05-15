# chat/routing.py
from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/messenger/<slug:sender_id>/<slug:receiver_id>', consumers.ChatConsumer),
]
