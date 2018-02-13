from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from Authenticate.models import LogIn

class SignUpFOrm(UserCreationForm):
    email = forms.EmailField(max_length=40,required=True,help_text='please enter a valid e-mail.')
    first_name = forms.CharField(max_length=30,required=True,help_text='Required.Enter your First Name')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.Enter your Last Name')

    class Meta:
        model = User
        fields = ('first_name','last_name','email','username','password1','password2')

class LoginForm(forms.ModelForm):

    class Meta:
        model = LogIn
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
        }