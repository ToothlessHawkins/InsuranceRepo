from django.db import models

# Create your models here.
class LogIn(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=50,)