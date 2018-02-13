from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Mechanic, Request, ServiceRep
from .forms import requestForm

"""AUTHENTICATION"""
from django.contrib.auth.decorators import user_passes_test
def not_serviceRep(user):
    if user:
        return user.groups.filter(name='ServiceRep').count() > 0
    return False

@user_passes_test(not_serviceRep, login_url='Authenticate:login')
def home(request):
    """Shitty authentication"""
    # thisRep = ServiceRep.objects.get(pk=request.user.username)
    # if not thisRep:
    #     return HttpResponseRedirect(reverse('customer:home'))
    mechanics_set = Mechanic.objects.all()
    request_set = Request.objects.all()
    return render(request, 'service/home.html', {'mechanics_set': mechanics_set, 'request_set':request_set})

@user_passes_test(not_serviceRep, login_url='Authenticate:login')
def request_details(request, req_id):
    req = get_object_or_404(Request, pk=req_id)
    return render(request, 'service/details.html', {'request': req})

@user_passes_test(not_serviceRep, login_url='Authenticate:login')
def newRequest(request):
    if request.method == 'POST':
        form = requestForm(request.POST)
        if form.is_valid():
            req = form.save(commit=False)
            req.save()
            # assign mechanic to job and job to mechanic here
            chosenMech = Mechanic.objects.get(id=req.mechanic.id)
            chosenMech.job = req
            chosenMech.save()
            return redirect('service:request_details', req_id=req.id)
    else:
        form = requestForm()
        """Use this to make sure the vehicles and drivers the user sees are only valid ones?"""
        # form.fields["employee"].queryset = Employee.objects.filter(department__name='Site_Survey')
        form.fields['mechanic'].queryset = Mechanic.objects.filter(job=None)
    return render(request, 'service/request.html', {'form':form})

@user_passes_test(not_serviceRep, login_url='Authenticate:login')
def complete_request(request, req_id):
    req = get_object_or_404(Request, pk=req_id)
    if (request.POST.get('mybtn')):
        # chosenMech = Mechanic.objects.get(id=req.mechanic.id)
        # chosenMech.job = None
        req.delete()
        return HttpResponseRedirect(reverse('service:home'))