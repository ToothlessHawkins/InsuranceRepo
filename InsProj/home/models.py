# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from policies.models import policy

# Create your models here.
class make_payment(models.Model):
    user_name = models.OneToOneField(policy, on_delete=models.CASCADE, primary_key=True)
    payment = models.PositiveSmallIntegerField()
