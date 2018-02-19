from django.urls import path

from . import views

app_name='service'
urlpatterns = [
    path('', views.home, name='home'),
    path('request/policy', views.request_policy, name='request_policy'),
    path('request/details/<req_id>/', views.request_details, name='request_details'),
    path('request/<req_id>/complete/', views.complete_request, name='complete_request'),
    path('request/<inPolicy>', views.newRequest, name='newRequest'),
]
