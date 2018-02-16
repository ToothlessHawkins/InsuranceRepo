from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('create_account/', views.create_account, name='create_account'),
    path('driver_details/', views.fill_driver_details, name='fill_driver_details'),
    path('vehicle_details/', views.fill_vehicle_details, name='fill_vehicle_details'),
    path('view_account_details/<user_name>/', views.view_account_details, name='view_account_details'),
    path('account_confirmation/', views.account_confirmation, name='account_confirmation'),
]
