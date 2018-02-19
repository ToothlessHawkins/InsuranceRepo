# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect
from policies.models import policy
from .forms import PolicyForm
from django.urls import reverse
import datetime

from accounts.models import account as acc

# Create your views here.
def view_holder_policies(request, policy_id):
    username = policy.objects.get(policy_id=policy_id)
    return render(request, 'view_holder_policies', {'username' : username})

def view_policy_details(request, first_name):
    policy_info = policy.objects.get(first_name=first_name)
    return render(request, 'view_policy_details.html', {'policy_info':policy_info})

def new_policy(request):
    if request.method == 'POST':
        form = PolicyForm(request.POST)
        if form.is_valid():
            policy = form.save(commit=False)
            currentUserAcc = acc.objects.get(user_name=request.user.username)
            policy.account = currentUserAcc
            # time = datetime.date.month if policy.payment_plan == 'M' else datetime.date. policy.payment_plan == 'Y'
            # policy.payment_due_date = policy.start_date + time
            policy.payment_due_date = datetime.date.today()
            div = 12 if policy.payment_plan == 'M' else 52 if policy.payment_plan =='W' else 1
            policy.balance = policy.total_rate / div
            policy.save()
            currentUserAcc.active_policy = policy.policy_id
            currentUserAcc.save()
            return HttpResponseRedirect(reverse('home:customer_home_page', kwargs={'user_name':request.user.username}))
    else:
        form = PolicyForm()

    return render(request, 'policies/policy_select.html', {'form':form})