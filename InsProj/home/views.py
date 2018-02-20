# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response,render, get_object_or_404
from policies.models import policy
from django.conf import settings
from accounts.models import account
from django.http import HttpResponseRedirect
import datetime
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from documents.models import Transaction

# Create your views here.
def customer_home_page(request):
    currentUser = request.user.username
    mypolicyid = policy.objects.get(account=account.objects.get(user_name=currentUser)).policy_id
    return render(request, 'home.html', {'currentUser' : currentUser, 'policy': mypolicyid})

def view_payment_history(request, pk):
    username = get_object_or_404(policy, pk=pk)
    return render(request, 'payment_history.html', {'username' : username})

def make_payment(request):
    # policy_id = request.session.get('policy_id')
    mypolicyid = policy.objects.get(account=account.objects.get(user_name=request.user.username)).policy_id
    policy_plan = get_object_or_404(policy, policy_id=mypolicyid)
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '{}'.format(policy.balance),
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
    currentUser = request.user.username
    currentAcc = account.objects.get(user_name=currentUser)
    activePolicy = policy.objects.get(account=currentAcc)

    payment = Transaction()
    payment.t_policy = activePolicy
    payment.t_account = currentAcc
    payment.PriorBalance = activePolicy.balance
    payment.NewBalance = 0
    payment.Amount = activePolicy.balance

    activePolicy.points += 1
    #increment payments_made
    activePolicy.payments_made += 1
    #figure out total number of payments based on payment plan
    #if there are more payments to be made if(total-paymments > 0)
    #set balance equal to new amount
    #increment due date based on payment plan
    activePolicy.balance = 0
    totalPayments = 12 if policy.payment_plan == 'M' else 52 if policy.payment_plan == 'W' else 1
    # time = datetime.week if activePolicy.payment_plan == 'W' else datetime.month if activePolicy.payment_plan == 'M' else datetime.MAXYEAR
    if activePolicy.payments_made == totalPayments:
        # stub for renewing policies
        activePolicy.payments_made = 0
    else:
        activePolicy.balance = activePolicy.total_rate / totalPayments
        time = datetime.timedelta(weeks=1) if activePolicy.payment_plan == 'W' \
            else datetime.timedelta(weeks=4) if activePolicy.payment_plan == 'M' \
            else datetime.timedelta(weeks=52)
        activePolicy.payment_due_date += time

    return render(request, 'payment_confirmation.html', {'currentUser' : currentUser,
                                                         'currentAcc' : currentAcc,
                                                         'activePolicy' : activePolicy,})

def on_time_payments(request):
    currentUser = request.user.username
    currentAcc = account.objects.get(user_name=currentUser)
    activePolicy = policy.objects.get(account=currentAcc)
    return render(request, 'on-time_payments.html', {'currentUser' : currentUser,
                                                'activePolicy' : activePolicy})

def due_payments(request):
    # username = policy.objects.get(pk=policy_id)
    currentUser = request.user.username
    currentAcc = account.objects.get(user_name=currentUser)
    activePolicy = policy.objects.get(account=currentAcc)
    #time = datetime.date.today() + datetime.timedelta(week=1) if activePolicy.payment_plan == 'W' else datetime.date.today() + datetime.timedelta(month=1) if activePolicy.payment_plan == 'M' else datetime.date.today()
    #account associated with username
    #active policy of that account
    due = False
    if datetime.date.today() > activePolicy.payment_due_date - datetime.timedelta(weeks=1):
        due = True

    return render(request, 'due_payments.html', {'currentUser' : currentUser,
                                                 'activePolicy' : activePolicy,
                                                 'due' : due})