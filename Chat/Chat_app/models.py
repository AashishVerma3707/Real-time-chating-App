from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.


class Room(models.Model):
    Name = models.CharField(max_length=1000)



class Message(models.Model):
    Value = models.CharField(max_length=100000)
    Time = models.DateTimeField(default=datetime.now, blank=True)
    User = models.CharField(max_length=1000)
    room = models.CharField(max_length=1000)

