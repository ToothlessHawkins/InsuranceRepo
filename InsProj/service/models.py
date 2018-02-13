from django.db import models

"""IMPORT MODELs FROM APPs HERE"""
# from policies.models import Policy
# from accounts.models import Vehicle, Driver

class Request(models.Model):
    # policy = models.ForeignKey('Policy', related_name='policy', on_delete=models.CASCADE,)
    # vehicle = models.ForeignKey('Vehicle', related_name='vehicle', on_delete=models.CASCADE,)
    # driver = models.ForeignKey('Driver', related_name='driver', on_delete=models.CASCADE,)
    location = models.TextField()
    date = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=250)
    mechanic = models.ForeignKey('Mechanic', related_name='mechanic', on_delete=models.CASCADE, null=True, blank=True)

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