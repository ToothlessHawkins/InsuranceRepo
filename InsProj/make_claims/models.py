from django.db import models
from policies.models import policy

# Create your models here.

class Claims(models.Model):
    Policy = models.ForeignKey(policy, related_name="claims_policy",on_delete=models.SET_NULL, null=True, blank=True)
    Claimed_Date = models.DateField()
    Claim_Id = models.CharField(max_length=20,primary_key=True)
    Other_party_Name = models.CharField(max_length=100)
    Other_party_Insurance_company_Name = models.CharField(max_length=100)
    Other_party_policy_Number = models.CharField(max_length=100)
    Other_party_Phone_Number = models.CharField(max_length=100)
    Claim_Resolved_Date = models.DateField(blank=True,null=True)
    Description = models.CharField(max_length=3000)
    Status = models.CharField(max_length= 500,blank=True,null=True)
    Adjuster_obj = models.CharField(max_length=50, null=True, blank=True)



