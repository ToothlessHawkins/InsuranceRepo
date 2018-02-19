from django.db import models

from policies.models import policy
from accounts.models import account

class Transaction(models.Model):
    t_policy = models.ForeignKey(policy, related_name='t_policy', on_delete=models.SET_NULL, null=True, blank=True)
    t_account = models.ForeignKey(account, related_name='t_account', on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(auto_now=True)
    PriorBalance = models.DecimalField(max_digits=8, decimal_places=2)
    NewBalance = models.DecimalField(max_digits=8, decimal_places=2)
    Amount = models.DecimalField(max_digits=8, decimal_places=2)



from documents.models import Transaction

payment = Transaction()
payment.t_policy = activePolicy
payment.t_account = currentAcc
payment.PriorBalance = activePolicy.balance
payment.NewBalance = 0
payment.Amount = activePolicy.balance