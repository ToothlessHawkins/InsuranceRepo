from django import forms
from make_claims.models import Claims

class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claims
        fields = ['Claimed_Date','Other_party_Name','Other_party_Insurance_company_Name',
                  'Other_party_policy_Number','Other_party_Phone_Number','Description']