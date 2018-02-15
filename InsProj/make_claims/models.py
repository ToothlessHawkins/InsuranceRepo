from django.db import models

# Create your models here.
class Vechicle(models.Model):
    pass

class Policy(models.Model):
    Policy_id = models.CharField(max_length=10,primary_key= True)
    points = models.IntegerField(default=0)

class Driver(models.Model):
    pass

class Claims(models.Model):
    # Vehicle = models.ForeignKey(Vechicle,on_delete=models.CASCADE)
    # Driver = models.ForeignKey(Driver,on_delete=models.CASCADE)
    # Policy = models.ForeignKey(Policy,on_delete=models.CASCADE)
    Claimed_Date = models.DateField()
    Claim_Id = models.CharField(max_length=20,primary_key=True)
    Other_party_Name = models.CharField(max_length=100)
    Other_party_Insurance_company_Name = models.CharField(max_length=100)
    Other_party_policy_Number = models.CharField(max_length=100)
    Other_party_Phone_Number = models.CharField(max_length=100)
    Claim_Resolved_Date = models.DateField(blank=True,null=True)
    Description = models.CharField(max_length=3000)
    Status = models.CharField(max_length= 500,blank=True,null=True)



