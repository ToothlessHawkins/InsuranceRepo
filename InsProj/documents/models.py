from django.db import models

from policies.models import policy
from accounts.models import account

class Transaction(models.Model):
    policy = models.ForeignKey('policies.policy', related_name='transaction_policy', on_delete=models.SET_NULL, null=True, blank=True)
    account = models.ForeignKey('accounts.account', related_name='transaction_account', on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(auto_now=True)
    PriorBalance = models.IntegerField()
    NewBalance = models.IntegerField()
    Amount = models.DecimalField(max_digits=8, decimal_places=2)