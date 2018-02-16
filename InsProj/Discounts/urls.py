from django.conf.urls import url
from django.urls import path
from Discounts.views import create_general_discounts,create_customer_discounts,view_customer_specific_discounts,view_general_discounts

urlpatterns = [
    url('create/general/discounts/',create_general_discounts,name = 'creategeneraldiscounts'),
    url('create/customer/discounts/',create_customer_discounts,name = 'createcustomerdiscounts'),
    url('view/general/discounts/',view_general_discounts,name='view_general_discounts'),
    path('view/customer/discounts/',view_customer_specific_discounts,name='view_customer_discounts'),
]