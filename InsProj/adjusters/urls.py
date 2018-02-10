from django.urls import path

from . import views

app_name='adjusters'
urlpatterns = [
    path('', views.home, name='home'),
    # path('<int:e_num>/', views.employee_details, name='employee_details'),
]
