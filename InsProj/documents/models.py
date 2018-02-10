from django.db import models

"""IMPORT MODELs FROM APPs HERE"""
# from policies.models import Policy
# from accounts.models import Account

class Transaction(models.Model):
    # policy = models.ForeignKey('Policy', related_name='policy', on_delete=models.CASCADE,)
    # account = models.ForeignKey('Account', related_name='account', on_delete=models.CASCADE,)
    date = models.DateField(auto_now=True)
    PriorBalance = models.IntegerField()
    NewBalance = models.IntegerField()
    Amount = models.DecimalField(max_digits=8, decimal_places=2)