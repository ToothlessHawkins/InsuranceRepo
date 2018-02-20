from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('customer/', views.customer_home_page, name='customer_home_page'),
    path('make_payment/', views.make_payment, name='make_payment'),
    path('payment_history/<pk>/', views.view_payment_history, name='view_payment_history'),
    path('payment_confirmation/', views.payment_confirmation, name='payment_confirmation'),
    path('on_time_payments/', views.on_time_payments, name='on_time_payments'),
    path('due_payments/', views.due_payments, name='due_payments'),
]

