from django.urls import path
from . import views

urlpatterns = [
    # path('/create_account/', create_account, name='create_account'),
    # path('/driver_details/', fill_driver_details, name='fill_driver_details'),
    # path('/vehicle_details/', fill_vehicle_details, name='fill_vehicle_details'),
    # path('/view_account_details/(?P<user_name>\D+)/$', include(urls), name='view_account_details'),
    path('create_account/', views.create_account, name='create_account'),
    path('driver_details/', views.fill_driver_details, name='fill_driver_details'),
    path('vehicle_details/', views.fill_vehicle_details, name='fill_vehicle_details'),
    path('view_account_details/<user_name>/', views.view_account_details, name='view_account_details'),
    path('account_confirmation/', views.account_confirmation, name='account_confirmation'),
]
