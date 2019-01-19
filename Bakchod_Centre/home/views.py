from django.shortcuts import render
from django.http import HttpResponse

def index1(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/home/signup"> signup </a>' )

def index2(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/home/user"> user </a>' )

def index3(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/home/user/edit"> useredit </a>' )

def index4(request):
    return HttpResponse('<h1>end</h1>' )
