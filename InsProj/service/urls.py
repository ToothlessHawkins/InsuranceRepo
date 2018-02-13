from django.urls import path

from . import views

app_name='service'
urlpatterns = [
    path('', views.home, name='home'),
    path('request/', views.newRequest, name='newRequest'),
    path('request/<req_id>/', views.request_details, name='request_details'),
    path('request/<req_id>/complete/', views.complete_request, name='complete_request'),
]
