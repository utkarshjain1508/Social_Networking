from django.db import models
from home.models import CustomUser
# Create your models here.
class Message(models.Model):
    Sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sender')
    Receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='receiver')
    MessageTime = models.DateTimeField(auto_now_add=True, editable=False)
    Description = models.CharField(max_length=1000)
