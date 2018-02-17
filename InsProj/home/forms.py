from django import forms
from home.models import make_payment

class MakePaymentForm(forms.ModelForm):

    class Meta:
        model = make_payment

        fields = [
            'policy_id',
            'payment_plan',
        ]