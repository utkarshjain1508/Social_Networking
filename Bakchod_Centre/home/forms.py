from django import forms
from .models import CustomUser

class signup_form(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'username', 'email', 'password', 'contact']

class user_edit_form(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'username', 'email', 'password', 'contact', 'profilePic']
