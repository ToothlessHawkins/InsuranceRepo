from django import forms

class statusForm(forms.Form):
    claimStatus = forms.CharField(label='Claim Status', max_length=500)