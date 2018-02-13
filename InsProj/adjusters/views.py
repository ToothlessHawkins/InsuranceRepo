from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import datetime

"""IMPORT W/E YOU NEED TO GET USERNAME"""

from .models import Adjuster
"""IMPORT CLAIM MODEL FROM CLAIMS APP HERE"""
# from claims.models import Claims

def home(request):
    adjuster_details = Adjuster.objects.get(pk=request.user.username)
    current_case = Claims.objects.get(pk=adjuster_details.claim.Claim_Id)
    return render(request, 'adjusters/home.html', {'adjuster_details':adjuster_details,'current_case': current_case})

def complete_case(request, Claim_Id):
    adjuster_details = Adjuster.objects.get(pk=request.user.username)
    claim = get_object_or_404(Claims, pk=Claim_Id)
    if (request.POST.get('mybtn')):
        # set the resolved date filed of the claim to today
        obj = claim.save(commit=False)
        obj.Claim_Resolved_Date = datetime.date.today()
        obj.save()
        # remove the claim from the adjuster's claim field
        adj = adjuster_details.save(commit=False)
        adj.claim = None
        adj.save()
        return HttpResponseRedirect(reverse('adjusters:home'))