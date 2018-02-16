from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('home/<user_name>/', views.customer_home_page, name='customer_home_page'),
    path('home/make_payment/', views.make_payment, name='make_payment'),
    path('home/payment_history/<pk>/', views.view_payment_history, name='view_payment_history'),
    path('payment_confirmation/', views.payment_confirmation, name='payment_confirmation'),
    path('home/on_time_payments/<pk>/', views.on_time_payments, name='on_time_payments'),
    path('home/due_payments/<pk>/', views.due_payments, name='due_payments'),
]

