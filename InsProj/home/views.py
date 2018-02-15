# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from policies.models import policy
from accounts.models import account
from django.http import HttpResponseRedirect
from .homes_forms import MakePaymentForm
from django.urls import reverse

# Create your views here.
def customer_home_page(request, user_name):
    username = account.objects.get(user_name=user_name)
    return render(request, 'home.html', {'username' : username})

def view_payment_history(request, pk):
    username = get_object_or_404(policy, pk=pk)
    return render(request, 'payment_history.html', {'username' : username})

def make_payment( request, user_name ):
    if request.method == 'GET':
        form = MakePaymentForm(request.GET)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.save()
            return HttpResponseRedirect(reverse('payment_confirmation'))
    else:
        form = MakePaymentForm()

    return render(request, 'make_payment.html', {'form':form})

def payment_confirmation(request):
    return render(request, 'payment_confirmation.html', {})

def on_time_payments(request, pk):
    username = policy.objects.get(pk=pk)
    return render(request, 'on-time_payments', {'username' : username})

def due_payments(request, pk):
    username = policy.objects.get(pk=pk)
    return render(request, 'due_payments', {'username' : username})