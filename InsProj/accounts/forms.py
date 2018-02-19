from django import forms
from accounts.models import account, driver, vehicle

class AccountsForm(forms.ModelForm):

    class Meta:
        model = account

        fields = [
            # 'first_name',
            # 'last_name',
            'corporation',
            'billing_address',
            'phone_number',
            # 'email_address',
            # 'user_name',
        ]

class DriverForm(forms.ModelForm):

    class Meta:
        model = driver

        fields = [
            'first_name',
            'last_name',
            'suffix',
            'driver_license_number',
            'gender',
            'active_driver',
            'driver_state_of_residence',
            'num_of_collisions',
        ]

class VehicleForm(forms.ModelForm):

    class Meta:
        model = vehicle

        fields = [
            'car_model',
            'year_of_purchase',
            'car_color',
            'car_condition',
            'car_condition_details',
            'car_mileage',
            'vehicle_num',
            'purchase_date',
            'miles_per_year',
        ]