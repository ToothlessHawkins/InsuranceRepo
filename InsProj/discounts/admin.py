from django.contrib import admin
from Discounts.models import Customer_Spcific_Discounts,Disconts_table,General_Discounts

# Register your models here.
admin.site.register(Customer_Spcific_Discounts)
admin.site.register(Disconts_table)
admin.site.register(General_Discounts)
