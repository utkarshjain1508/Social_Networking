from django.shortcuts import render
from django.http import HttpResponse
from .models import CustomUser
from django.contrib.auth import authenticate
from .forms import signup_form

def signup(request):
    if request.method == 'GET':
        New_Form = signup_form()
        return render(request, 'home/signup.html')
    elif request.method == 'POST':
        form = signup_form(request.POST)

        if form.is_valid():
            if form.cleaned_data.get('password') != form.cleaned_data.get('password2'):
                print("Error! Password Not Matched")
                pass
            else:
                # New_User = CustomUser()
                form.save()
                # New_User.username = form.cleaned_data['username']
                # New_User.first_name = form.cleaned_data['first_name']
                # New_User.last_name = form.cleaned_data['last_name']
                # New_User.email = form.cleaned_data['email']
                # New_User.password = form.cleaned_data['password']
                # New_User.contact = form.cleaned_data['contact']
                # New_User.save()
                return render(request, 'home/login.html')
        else:
            print("wrong")
            return render(request,'home/signup.html')

def profile(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        username = request.GET['username']

        # friends = get_object_or_404()
        return render(request, 'home/profile.html', {'person': person})

def user_edit(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        return render(request, 'home/user_edit.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                custom_user = CustomUser.objects.filter(username=username)
                return render(request, 'home/profile.html', {'custom_user': custom_user})
            else:
                return render(request, 'home/login.html', {'error_message': 'Your account has been disabled.'})
        else:
            return render(request, 'home/login.html', {'error_message': 'Invalid login'})

    elif request.method == 'GET':
        return render(request, 'home/login.html', {})
