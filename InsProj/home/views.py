# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from policies.models import policy
from accounts.models import account
from django.http import HttpResponse

# Create your views here.
def customer_home_page(request, user_name):
    username = account.objects.get(user_name=user_name)
    return render(request, 'home.html', {'username' : username})

def create_account(request):
    if request.method == "GET":
        if request.GET.get("firstname"):
            if request.GET.get("lastname"):
                if request.GET.get("corporation"):
                    if request.GET.get("billing_address"):
                        if request.GET.get("phone_number"):
                            if request.GET.get("email_address"):
                                accounts = account()
                                accounts.first_name = request.GET.get("firstname")
                                accounts.last_name = request.GET.get("lastname")
                                accounts.corporation = request.GET.get("corporation")
                                accounts.billing_address = request.GET.get("billing_address")
                                accounts.phone_number = request.GET.get("phone_number")
                                accounts.email_address = request.GET.get("email_address")
                                accounts.save()
                                return HttpResponse("Account has been created!")
        else:
            return render(request, 'create_account.html')

def view_payment_history(request, pk):
    username = get_object_or_404(policy, pk=pk)
    return render(request, 'payment_history.html', {'username' : username})

def make_payment(request):
    if request.method == 'GET':
        return render(request, 'make_payment.html', {})
    '''elif request.method == 'POST':
        print('request.method == post')
        if request.GET.get('user_name'):
            print('request.GET.get(user_name)')
            if request.GET.get('payment'):
                print('request.GET.get(payment)')
                username = policy.objects.get(user_name=request.GET.get('user_name'))
      # user_rate = policy.objects.filter(pk=pk).get(total_rate='total_rate')
                user_rate = policy.objects.get(user_name=request.GET.get('user_name')).total_rate
      # user_payment = policy.objects.filter(pk).get(payment='payment')
                user_payment = policy.objects.get(user_name=request.GET.get('user_name')).payment
      # num_of_payments = policy.objects.filter(pk).get(payments_made='payments_made')
                num_of_payments = policy.objects.get(user_name=request.GET.get('user_name')).payments_made
            # if request.GET.get('payment'):
                if request.GET.get('payment') >= user_rate:
                    user_payment += request.GET.get('payment')
                    num_of_payments += 1
                    return render(request, 'payment_confirmation.html', {'username' : username,
                                                               'user_rate' : user_rate,
                                                               'user_payments' : user_payment,
                                                               'num_of_paymnets' : num_of_payments,})
    return HttpResponse("View Method Failed")'''

def payment_confirmation(request):
    return render(request, 'payment_confirmation.html', {})

def on_time_payments(request, pk):
    username = policy.objects.get(pk=pk)
    return render(request, 'on-time_payments', {'username' : username})

def due_payments(request, pk):
    username = policy.objects.get(pk=pk)
    return render(request, 'due_payments', {'username' : username})