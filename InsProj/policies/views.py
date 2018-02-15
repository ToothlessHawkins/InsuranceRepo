# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from policies.models import policy

# Create your views here.
def view_holder_policies(request, policy_id):
    username = policy.objects.get(policy_id=policy_id)
    return render(request, 'view_holder_policies', {'username' : username})