from django.db import models
from django import forms

class Person(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100, widget=forms.PasswordInput)
    contact = models.IntegerField(max_length=20)
    profilePic = models.ImageField(upload_to='/media/', null=True)  # Check upload_to

    listOfFriends = models.ArrayField(
        models.CharField(max_length=100)
    )
