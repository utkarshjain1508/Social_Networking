from django.shortcuts import render
from django.http import HttpResponse

def signup(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/home/signup"> signup </a>' )

def profile(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/home/user"> profile </a>' )

def useredit(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/home/user/edit"> useredit </a>' )

def login(request):
    return HttpResponse('<h1>end</h1>')
