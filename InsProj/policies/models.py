# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from accounts.models import account

# Create your models here.
class policy(models.Model):
    user_name = models.OneToOneField(account, on_delete=models.CASCADE)
    policy_id = models.AutoField(primary_key=True)
    POLICY_CHOICES = (
        ('LC', 'Liability Coverage'),
        ('CC', 'Collision Coverage'),
        ('COM', 'Comprehensive Coverage'),
        ('UN', 'Uninsured/Underinsured Motorist Coverage'),
        ('MP','Medical Payments'),
        ('PIP', 'Personal Injury Protection'),
    )
    policy_plan = models.CharField(max_length=100, choices=POLICY_CHOICES)
    payments_made = models.IntegerField(default=0)
    total_rate = models.PositiveSmallIntegerField()
    PLAN_OPTIONS = (
        ('Y', 'Yearly'),
        ('M', 'Monthly'),
        ('W', 'Weekly'),
    )
    payment_plan = models.CharField(max_length=10, choices=PLAN_OPTIONS, default='Yearly')
    payment_due_date = models.DateTimeField()
    payment = models.PositiveSmallIntegerField(default=0)
    actual_date_of_payment = models.DateTimeField()
    YES_NO_OPTIONS = (
        ('Y','Yes'),
        ('N','No'),
    )
    suspended = models.CharField(max_length=3, choices=YES_NO_OPTIONS)
    points = models.IntegerField(default=0)

    def __str__(self):
        return "{}".format(self.user_name)


