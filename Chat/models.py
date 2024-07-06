from django.db import models
from datetime import datetime


class Room(models.Model):
    room = models.CharField(max_length=1000000)

    def __str__(self) -> str:
        return self.room


class Message(models.Model):
    message= models.CharField(max_length=5000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=100)
    room = models.CharField(max_length=1000000)
    
    
