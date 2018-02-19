from django.contrib import admin

from . import models

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['t_policy', 't_account', 'date', 'PriorBalance', 'NewBalance', 'Amount']
admin.site.register(models.Transaction, TransactionAdmin)