from django import forms
from .models import Request

class requestForm(forms.ModelForm):
    class Meta:
        model = Request
        # 'policy', 'vehicle', 'driver',
        fields=('location','description','mechanic')