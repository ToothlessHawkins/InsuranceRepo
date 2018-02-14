from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import datetime

from .models import Adjuster
from make_claims.models import Claims

"""AUTHENTICATION"""
from django.contrib.auth.decorators import user_passes_test
def not_adjuster(user):
    if user:
        return user.groups.filter(name='Adjuster').count() > 0
    return False

@user_passes_test(not_adjuster, login_url='Authenticate:login')
def home(request):
    adjuster_details = Adjuster.objects.get(pk=request.user.username)
    current_case = None
    if adjuster_details.claim:
        current_case = Claims.objects.get(pk=adjuster_details.claim.Claim_Id)
    return render(request, 'adjusters/home.html', {'adjuster_details':adjuster_details,'current_case': current_case})

@user_passes_test(not_adjuster, login_url='Authenticate:login')
def complete_case(request, Claim_Id):
    adjuster_details = Adjuster.objects.get(pk=request.user.username)
    claim = get_object_or_404(Claims, pk=Claim_Id)
    if (request.POST.get('mybtn')):
        # set the resolved date filed of the claim to today
        claim.Claim_Resolved_Date = datetime.date.today()
        claim.save()

        # remove the claim from the adjuster's claim field
        adjuster_details.claim = None
        """auto assign claim to adjuster here"""
        # #get first claim in set of claims with no adjuster
        # pendingClaim = Claims.objects.filter(adjuster=None)[0]
        # #assign a pending claim, if there is one
        # if pendingClaim:
        #     adjuster_details.claim = pendingClaim
        adjuster_details.save()
        return HttpResponseRedirect(reverse('adjusters:home'))