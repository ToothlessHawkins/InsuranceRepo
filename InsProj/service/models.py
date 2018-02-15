from django.db import models

from policies.models import policy
from accounts.models import driver#, vehicle

class Request(models.Model):
    policy = models.ForeignKey('policies.Policy', related_name='policy', on_delete=models.SET_NULL, null=True, blank=True)
    # vehicle = models.ForeignKey('accounts.Vehicle', related_name='vehicle', on_delete=models.SET_NULL,)
    driver = models.ForeignKey('accounts.Driver', related_name='driver', on_delete=models.SET_NULL, null=True, blank=True)
    location = models.TextField()
    date = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=250)
    mechanic = models.ForeignKey('Mechanic', related_name='mechanic', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.date)

class Mechanic(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    job = models.ForeignKey('Request', related_name='job', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class ServiceRep(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name