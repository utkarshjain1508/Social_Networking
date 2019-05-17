from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    contact = models.IntegerField(default=0)
    profile_image = models.ImageField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    education = models.CharField(max_length=300, blank=True)
    job = models.CharField(max_length=300, blank=True)
    education_place = models.CharField(max_length=300, blank=True)
    job_place = models.CharField(max_length=300, blank=True)
    current_location = models.CharField(max_length=300, blank=True)
    gender = models.CharField(max_length=100)
    relationship_status = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username

class Connection(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='friend_user')
    friend = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='friend_friend')
    connection_time = models.DateTimeField(auto_now_add=True, editable=False)
    status = models.CharField(max_length=100)

class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='post_user')
    post = models.CharField(max_length=1000)
    post_time = models.DateTimeField(auto_now_add=True, editable=False)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_key')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comment_user')
    comment = models.CharField(max_length=1000)
    comment_time = models.DateTimeField(auto_now_add=True, editable=False)
