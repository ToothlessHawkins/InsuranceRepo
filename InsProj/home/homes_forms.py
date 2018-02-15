from django import forms
from policies.models import policy

class MakePaymentForm(forms.ModelForm):

    class Meta:
        model = policy

        fields = [
            'user_name',
            'payment',
        ]