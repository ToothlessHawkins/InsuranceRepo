from django.urls import path

from . import views

app_name='adjusters'
urlpatterns = [
    path('', views.home, name='home'),
    path('complete/<Claim_Id>', views.complete_case, name='complete_case')
]
