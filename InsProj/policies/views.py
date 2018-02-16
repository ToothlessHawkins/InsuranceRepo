# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from policies.models import policy

# Create your views here.
def view_holder_policies(request, policy_id):
    username = policy.objects.get(policy_id=policy_id)
    return render(request, 'view_holder_policies', {'username' : username})

def view_policy_details(request, user_name):
    policy_info = policy.objects.get(user_name=user_name)
    return render(request, 'view_policy_details.html', {'policy_info':policy_info})
