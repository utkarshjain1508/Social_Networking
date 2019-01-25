from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import UpdateView

def signup(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/home/signup"> signup </a>' )

def profile(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/home/user"> profile </a>' )

class UserEdit(UpdateView):
    model = Person
    fields = ['profilePic', 'name', 'username', 'email', 'contact']

def login(request):
    return HttpResponse('<h1>end</h1>')
