from django.db import models
from django import forms

class Person(models.Model):

    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100, widget=forms.PasswordInput)
    contact = models.IntegerField(max_length=20)
    profilePic = models.ImageField(upload_to='/media/', null=True)  # Check upload_to

<<<<<<< HEAD
    # listOfFriends = models.ArrayField(
    #     models.ForeignKey(Person)
    # )
=======
    listOfFriends = models.ArrayField(
        models.CharField(max_length=100)
    )
    
>>>>>>> 9cc62befb487f7193859cc6a72d6df26ddbb03cd
