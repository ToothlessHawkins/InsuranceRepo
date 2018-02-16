# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from accounts.models import account

class policy(models.Model):
    account = models.ForeignKey(account, related_name='account', on_delete=models.SET_NULL, null=True)
    policy_id = models.AutoField(primary_key=True)
    start_date = models.DateField(auto_now=True)
    # POLICY_CHOICES = (
    #     ('LC', 'Liability Coverage'),
    #     ('CC', 'Collision Coverage'),
    #     ('COM', 'Comprehensive Coverage'),
    #     ('UN', 'Uninsured/Underinsured Motorist Coverage'),
    #     ('MP','Medical Payments'),
    #     ('PIP', 'Personal Injury Protection'),
    # )
    # policy_plan = models.CharField(max_length=100, choices=POLICY_CHOICES)
    payments_made = models.IntegerField(default=0)
    PRICE_OPTIONS = (
        ('12000.00', 'Full'),
        ('6000.00', 'Half'),
        ('3000.00', 'Liability'),
    )
    total_rate = models.DecimalField(max_digits=8, decimal_places=2, choices=PRICE_OPTIONS)
    PLAN_OPTIONS = (
        ('Y', 'Yearly'),
        ('M', 'Monthly'),
        ('W', 'Weekly'),
    )
    payment_plan = models.CharField(max_length=1, choices=PLAN_OPTIONS, default='Yearly')
    payment_due_date = models.DateField()
    balance = models.DecimalField(max_digits=8, decimal_places=2)
    # actual_date_of_payment = models.DateTimeField()
    suspended = models.BooleanField(default=False)
    points = models.IntegerField(default=0)

    def __str__(self):
        return "{}".format(self.policy_id)


