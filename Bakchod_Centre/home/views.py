from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

def signup(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/home/signup"> signup </a>' )

def profile(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        person = request.person

        # friends = get_object_or_404()
        return render(request, 'home/profile.html', {'person': person})

def useredit(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        return render(request, 'home/user-edit.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                person = Person.objects.filter(user=request.user)
                return render(request, 'home/profile.html', {'person': person})
            else:
                return render(request, 'home/login.html', {'error_message': 'Your account has been disabled.'})
        else:
            return render(request, 'home/login.html', {'error_message': 'Invalid login'})

    elif request.method == 'GET':
        return render(request, 'home/login.html')
