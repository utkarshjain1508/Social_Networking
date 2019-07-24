# messenger/urls.py
from django.urls import path

from . import views

app_name = 'messenger'

urlpatterns = [
    path('<slug:sender_id>', views.index, name='index'),
]
