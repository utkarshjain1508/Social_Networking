from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser

<<<<<<< HEAD
class Person(models.Model):
=======
class CustomUser(AbstractUser):
>>>>>>> 811965d3771fd182064b97de3cd3156755217dbd
    name = models.CharField(max_length=100)
    contact = models.IntegerField(max_length=20)
    profilePic = models.ImageField(upload_to='/media/', null=True)

    def __str__(self):
        return self.username

<<<<<<< HEAD
    # listOfFriends = models.ArrayField(
    #     models.CharField(max_length=100)
    # )
=======
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
>>>>>>> 811965d3771fd182064b97de3cd3156755217dbd
