from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import datetime

from .models import Adjuster
from make_claims.models import Claims

def home(request):
    """GET USERNAME"""
    # adjuster_details = Adjuster.objects.get(pk=request.user.username)
    adjuster_details = Adjuster.objects.get(pk='banana')
    current_case = None
    if adjuster_details.claim:
        current_case = Claims.objects.get(pk=adjuster_details.claim.Claim_Id)
    return render(request, 'adjusters/home.html', {'adjuster_details':adjuster_details,'current_case': current_case})

def complete_case(request, Claim_Id):
    """GET USERNAME"""
    # adjuster_details = Adjuster.objects.get(pk=request.user.username)
    adjuster_details = Adjuster.objects.get(pk='banana')

    claim = get_object_or_404(Claims, pk=Claim_Id)
    if (request.POST.get('mybtn')):
        # set the resolved date filed of the claim to today
        claim.Claim_Resolved_Date = datetime.date.today()
        claim.save()
        # remove the claim from the adjuster's claim field
        adjuster_details.claim = None
        adjuster_details.save()
        return HttpResponseRedirect(reverse('adjusters:home'))