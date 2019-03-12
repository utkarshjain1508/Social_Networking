from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    contact = models.IntegerField(default=0)
    profile_image = models.ImageField(null=True, blank=True)
    date_of_birth = models.DateField()
    education = models.CharField(max_length=300, blank=True)
    job = models.CharField(max_length=300, blank=True)
    education_place = models.CharField(max_length=300, blank=True)
    job_place = models.CharField(max_length=300, blank=True)
    current_location = models.CharField(max_length=300, blank=True)
    gender = models.CharField(max_length=100)
    relationship_status = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username
