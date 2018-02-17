from django.urls import path
from . import views

app_name='policies'
urlpatterns = [
    path('new/', views.new_policy, name='new_policy'),
    path('view_holder_policies/<policy_id>/', views.view_holder_policies, name='view_holder_policies'),
    path('view_policy_details/<first_name>/', views.view_policy_details, name='view_policy_details'),
]
