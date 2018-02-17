from django import forms
from policies.models import policy

class PolicyForm(forms.Form):

    class Meta:
        model = policy

        fields = [
            'total_rate'
            'payment_plan',
        ]
