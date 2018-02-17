# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from policies.models import policy
from django.conf import settings
# from accounts.models import account
from django.http import HttpResponseRedirect
# from .forms import MakePaymentForm
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm

# Create your views here.
def customer_home_page(request):
    # username = account.objects.get(user_name=user_name)
    return render(request, 'home.html', {})

def view_payment_history(request, pk):
    username = get_object_or_404(policy, pk=pk)
    return render(request, 'payment_history.html', {'username' : username})

def make_payment(request):
    policy_id = request.session.get('policy_id')
    policy_plan = policy.objects.get(policy, id=policy_id)
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '{}'.format(policy.total_rate),
        'policy': 'Policy {}'.format(policy.policy_id),
        'invoice': str(policy.policy_id),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('home:payment_confirmation')),
        'cancel_return': 'http://{}{}'.format(host, reverse('home:payment_canceled'))
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'home/payment_process.html', {'policy_plan': policy_plan,
                                                         'form': form})

def payment_confirmation(request):
    return render(request, 'payment_confirmation.html', {})

def on_time_payments(request, pk):
    username = policy.objects.get(pk=pk)
    return render(request, 'on-time_payments', {'username' : username})

def due_payments(request, pk):
    username = policy.objects.get(pk=pk)
    username.points += 1
    return render(request, 'due_payments', {'username' : username})