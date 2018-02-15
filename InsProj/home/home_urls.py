"""Insurance_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from home.views import *
from home import views
from Insurance_Project import urls

urlpatterns = [
    url(r'/admin/', admin.site.urls),
    url(r'/home/(?P<user_name>\D+)/$', customer_home_page, name='customer_home_page'),
    url(r'/home/make_payment/', make_payment, name='make_payment'),
    url(r'/home/payment_history/(?P<pk>\d+)/$', view_payment_history, name='view_payment_history'),
    url(r'/payment_confirmation/', views.payment_confirmation, name='payment_confirmation'),
    url(r'/home/on_time_payments/(?P<pk>\d+)$', on_time_payments, name='on_time_payments'),
    url(r'/home/due_payments/(?P<pk>\d+)$', due_payments, name='due_payments'),
]
