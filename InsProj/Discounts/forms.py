from django import forms
from Discounts.models import General_Discounts,Disconts_table,Customer_Spcific_Discounts

class General_Disounts_Form(forms.ModelForm):
    class Meta:
        model = General_Discounts
        exclude = ['Cupon_Code',]

# class Customer_Specific_Discount_Form(forms.ModelForm):
#     class Meta:
#         model = Customer_Spcific_Discounts
#         fields = '__all__'

class Discount_Table_Form(forms.ModelForm):
    class Meta:
        model  = Disconts_table
        exclude = ['Cupon_Code',]