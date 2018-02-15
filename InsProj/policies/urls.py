from django.urls import path
from . import views

app_name='policies'
urlpatterns = [
    path('view_holder_policies/<policy_id>/', views.view_holder_policies, name='view_holder_policies'),
]
