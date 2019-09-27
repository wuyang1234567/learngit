from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class user(models.Model):
    usernames=models.CharField(max_length=30)
    passwords = models.CharField(max_length=8)
    emails = models.CharField(max_length=50)
    times = models.DateTimeField()

class name(models.Model):
    usernames = models.CharField(max_length=30)
    password = models.CharField(max_length=8)
    email = models.CharField(max_length=50)
    time = models.DateTimeField()