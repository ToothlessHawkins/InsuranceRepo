from django import forms
from .models import policy

class PolicyForm(forms.ModelForm):

    class Meta:
        model = policy
        fields=('total_rate','payment_plan')
