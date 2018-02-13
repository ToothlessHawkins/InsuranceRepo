# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class account(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    account_id = models.IntegerField(auto_created=True, default="0", null=True)
    corporation = models.CharField(max_length=50)
    billing_address = models.CharField(max_length=50)
    phone_number = models.BigIntegerField()
    email_address = models.EmailField()
    user_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return "{}".format(self.user_name)

class driver(models.Model):
    first_name = models.ForeignKey(account, related_name="firstname", on_delete=models.SET_NULL, null=True)
    last_name = models.ForeignKey(account, related_name="lastname", on_delete=models.SET_NULL, null=True)
    user_name = models.ForeignKey(account, related_name="username", on_delete=models.SET_NULL, null=True)
    suffix = models.CharField(max_length=50)
    license_plate_num = models.CharField(max_length=7)
    GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('n', 'prefer not to answer'),
         )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='n')
    DRIVER_CHOICES = (
        ('LP', 'Learners Permits'),
        ('DL', 'Drivers License'),
        ('R', 'Revoked'),
        ('S', 'Suspended'),
    )
    active_driver = models.CharField(max_length=2, choices=DRIVER_CHOICES)
    driver_state_of_residence = models.CharField(max_length=50)
    num_of_collisions = models.IntegerField(default=0)

    def __str__(self):
        return "{}".format(self.user_name)
