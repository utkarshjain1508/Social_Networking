from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    contact = models.IntegerField(default=0)
    profile_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.username
