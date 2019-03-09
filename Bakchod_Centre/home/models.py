from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    contact = models.IntegerField(default=0)
    profilePic = models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self):
        return self.username
