from django import forms
from policies.models import policy

class PolicyForm(forms.Form):

    class Meta:
        model = policy

        fields = [
            'user_name',
            'account_id',
            'policy_plan',
            'payments_made',
            'total_rate',
            'payment_plan',
            'payment_due_date',
            'payment',
            'actual_date_of_payment',
            'suspended',
            'points',
        ]