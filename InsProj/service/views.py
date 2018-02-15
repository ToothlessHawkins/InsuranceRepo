from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Mechanic, Request, ServiceRep
from .forms import requestForm, policyForm
from policies.models import policy

"""AUTHENTICATION"""
from django.contrib.auth.decorators import user_passes_test
def not_serviceRep(user):
    if user:
        return user.groups.filter(name='ServiceRep').count() > 0
    return False

@user_passes_test(not_serviceRep, login_url='Authenticate:login')
def home(request):
    mechanics_set = Mechanic.objects.all()
    request_set = Request.objects.all()
    return render(request, 'service/home.html', {'mechanics_set': mechanics_set, 'request_set':request_set})

@user_passes_test(not_serviceRep, login_url='Authenticate:login')
def request_details(request, req_id):
    req = get_object_or_404(Request, pk=req_id)
    return render(request, 'service/details.html', {'request': req})

@user_passes_test(not_serviceRep, login_url='Authenticate:login')
def request_policy(request):
    if request.method == 'POST':
        form = policyForm(request.POST)
        if form.is_valid():
            policy_num = form.cleaned_data['policyNum']
            chosenPolicy = get_object_or_404('policy', Policy_Number=policy_num)
            return redirect('service:newRequest', policy=chosenPolicy)
    else:
        form = policyForm()
    return render(request, 'service/request.html', {'form':form})

@user_passes_test(not_serviceRep, login_url='Authenticate:login')
def newRequest(request, inPolicy):
    if request.method == 'POST':
        form = requestForm(request.POST)
        if form.is_valid():
            req = form.save(commit=False)
            req.policy = inPolicy
            req.save()
            # assign mechanic to job and job to mechanic here
            chosenMech = Mechanic.objects.get(id=req.mechanic.id)
            chosenMech.job = req
            chosenMech.save()
            return redirect('service:request_details', req_id=req.id)
    else:
        form = requestForm()
        """Use this to make sure the vehicles and drivers the user sees are only valid ones"""
        # form.fields["driver"].queryset = driver.objects.filter(account=inPolicy.account)
        # form.fields["vehicle"].queryset = vehicle.objects.filter(account=inPolicy.account)
        form.fields['mechanic'].queryset = Mechanic.objects.filter(job=None)
    return render(request, 'service/request.html', {'form':form})

@user_passes_test(not_serviceRep, login_url='Authenticate:login')
def complete_request(request, req_id):
    req = get_object_or_404(Request, pk=req_id)
    if (request.POST.get('mybtn')):
        req.delete()
        return HttpResponseRedirect(reverse('service:home'))