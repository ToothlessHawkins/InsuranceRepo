from django.db import models

from policies.models import Policy
from accounts.models import Account

class Transaction(models.Model):
    policy = models.ForeignKey('policies.Policy', related_name='policy', on_delete=models.SET_NULL,)
    account = models.ForeignKey('accounts.Account', related_name='account', on_delete=models.SET_NULL,)
    date = models.DateField(auto_now=True)
    PriorBalance = models.IntegerField()
    NewBalance = models.IntegerField()
    Amount = models.DecimalField(max_digits=8, decimal_places=2)