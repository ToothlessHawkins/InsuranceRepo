from django.db import models
from policies.models import policy

# Create your models here.
class General_Discounts(models.Model):
    Discount_Name = models.CharField(max_length=20)
    Start_Date = models.DateField()
    End_Date = models.DateField()
    Cupon_Code = models.CharField(max_length=10,primary_key=True)

class Disconts_table(models.Model):
    Discount_Name = models.CharField(max_length=20)
    points_required = models.IntegerField()
    Cupon_Code = models.CharField(max_length=10,primary_key=True)

class Customer_Spcific_Discounts(models.Model):
    Policy_Id = models.ForeignKey(policy,on_delete=models.CASCADE)
    Discount_Name = models.ForeignKey(Disconts_table,on_delete=models.CASCADE)



