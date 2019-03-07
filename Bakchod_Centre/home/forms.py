from django import forms
from .models import CustomUser

class signup_form(forms.ModelForm):
    password2 = forms.CharField(label='password2', max_length=100)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'contact']

class user_edit_form(forms.ModelForm):
    password2 = forms.CharField(label='password2', max_length=100)
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'contact', 'profilePic']
