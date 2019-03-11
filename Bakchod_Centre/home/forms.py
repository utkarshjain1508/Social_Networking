from django import forms
from .models import CustomUser
from django.db import models

class signup_form(forms.Form):
    password2 = forms.CharField(label='password2', max_length=100)
    password = forms.CharField(label='password', max_length=100)
    first_name = forms.CharField(label='first_name', max_length=100)
    last_name = forms.CharField(label='last_name', max_length=100)
    username = forms.CharField(label='username', max_length=100)
    email = forms.CharField(label='email', max_length=100)
    contact = forms.IntegerField(label='contact') 

class user_edit_form(forms.Form):
    first_name = forms.CharField(label='first_name', max_length=100)
    last_name = forms.CharField(label='last_name', max_length=100)
    username = forms.CharField(label='username', max_length=100)
    email = forms.CharField(label='email', max_length=100)
    contact = forms.IntegerField(label='contact')
    profilePic = models.ImageField(upload_to='media/', null=True, blank=True)

class change_password_form(forms.Form):
    old_password = forms.CharField(label='old_password', max_length=100)
    new_password = forms.CharField(label='new_password', max_length=100)
    confirm_password = forms.CharField(label='confirm_password', max_length=100)
