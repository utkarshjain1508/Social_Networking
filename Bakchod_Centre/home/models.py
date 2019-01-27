from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    contact = models.IntegerField(default=0)
    profilePic = models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self):
        return self.username

# class Person(models.Model):
#
#     name = models.CharField(max_length=100)
#     username = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     password = models.CharField(max_length=100, widget=forms.PasswordInput)
#     contact = models.IntegerField(max_length=20)
#     profilePic = models.ImageField(upload_to='/media/', null=True)  # Check upload_to
#
#     # listOfFriends = models.ArrayField(
#     #     models.ForeignKey(Person)
#     # )
