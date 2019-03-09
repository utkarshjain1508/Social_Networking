from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CustomUser
from django.contrib.auth import authenticate, login
from .forms import signup_form, user_edit_form, change_password_form
from django.contrib.auth.hashers import make_password

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
                New_User = CustomUser()
                New_User.username = form.cleaned_data['username']
                New_User.first_name = form.cleaned_data['first_name']
                New_User.last_name = form.cleaned_data['last_name']
                New_User.email = form.cleaned_data['email']
                dum = make_password(form.cleaned_data['password'])
                New_User.password = dum
                New_User.contact = form.cleaned_data['contact']
                New_User.save()
                return render(request, 'home/login.html')
        else:
            return render(request,'home/signup.html')

def profile(request, userName):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        custom_user = CustomUser.objects.get(username = userName)
        return render(request, 'home/profile.html', {'custom_user': custom_user})

def user_edit(request, userName):
    if request.method == 'POST':
        form = user_edit_form(request.POST)
        print("yes")
        if form.is_valid():
            print("no")
            Edit_User = CustomUser.objects.get(username = userName)
            Edit_User.username = form.cleaned_data['username']
            Edit_User.first_name = form.cleaned_data['first_name']
            Edit_User.last_name = form.cleaned_data['last_name']
            Edit_User.email = form.cleaned_data['email']
            Edit_User.contact = form.cleaned_data['contact']
            Edit_User.save()
            return redirect('/home/'+userName)

    elif request.method == 'GET':
        newForm = user_edit_form()
        custom_user = CustomUser.objects.get(username = userName)
        return render(request, 'home/user_edit.html', {'custom_user': custom_user})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                custom_user = CustomUser.objects.filter(username=username)
                return redirect('/home/'+username)
            else:
                return render(request, 'home/login.html', {'error_message': 'Your account has been disabled.'})
        else:
            return render(request, 'home/login.html', {'error_message': 'Invalid login'})

    elif request.method == 'GET':
        return render(request, 'home/login.html', {})


def change_password(request, userName):
    if request.method == 'POST':
        form = change_password_form(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password']
            confirm_password = form.cleaned_data['confirm_password']
            custom_user = CustomUser.objects.get(username=userName)
            change_user = authenticate(username=userName, password=old_password)
            if change_user is None:
                return render(request, 'home/change_password.html', {'custom_user': custom_user, 'error_message': 'You entered incorrect old password.'})

            if new_password != confirm_password:
                return render(request, 'home/change_password.html', {'custom_user': custom_user, 'error_message': 'Your new passwords do not match.'})

            change_user.set_password(new_password)
            change_user.save()
            return redirect('/home/'+userName)

    elif request.method == 'GET':
        newForm = change_password_form()
        custom_user = CustomUser.objects.get(username = userName)
        return render(request, 'home/change_password.html', {'custom_user': custom_user})
