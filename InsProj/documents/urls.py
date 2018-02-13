from django.urls import path

from . import views

app_name='documents'
urlpatterns = [
    path('', views.home, name='home'),
    path('billing/', views.billing_statements, name='billing_statements'),
    # path('claims/', views.claim_details, name='claim_details'),
]
