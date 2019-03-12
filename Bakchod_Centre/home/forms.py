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
    date_of_birth = forms.DateField(label='date_of_birth')
    gender = forms.CharField(max_length=100, label='gender')

class user_edit_form(forms.Form):
    first_name = forms.CharField(label='first_name', max_length=100)
    last_name = forms.CharField(label='last_name', max_length=100)
    username = forms.CharField(label='username', max_length=100)
    email = forms.CharField(label='email', max_length=100)
    contact = forms.IntegerField(label='contact')
    profilePic = forms.ImageField(label='profile_image', required=False)
    date_of_birth = forms.DateField(label='date_of_birth')
    gender = forms.CharField(max_length=100, label='gender')
    education = forms.CharField(label='education', required=False)
    job = forms.CharField(label='job', required=False)
    education_place = forms.CharField(label='education_place', required=False)
    job_place = forms.CharField(label='job_place', required=False)
    current_location = forms.CharField(label='current_location', required=False)
    relationship_status = forms.CharField(label='relationship_status', required=False)

class change_password_form(forms.Form):
    old_password = forms.CharField(label='old_password', max_length=100)
    new_password = forms.CharField(label='new_password', max_length=100)
    confirm_password = forms.CharField(label='confirm_password', max_length=100)
