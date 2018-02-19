from django import forms
from .models import Request

class requestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields=('driver', 'vehicle', 'location','description','mechanic',)

class policyForm(forms.Form):
    policyNum = forms.CharField(label='Policy Number', max_length=100)