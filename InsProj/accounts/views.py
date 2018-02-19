# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import account, driver, vehicle
from .forms import AccountsForm, DriverForm, VehicleForm

# Create your views here.
def create_account(request):
    if request.method == 'POST':
        form = AccountsForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.first_name = request.user.first_name
            account.last_name = request.user.last_name
            account.email_address = request.user.email
            account.user_name =request.user.username
            account.save()
            return HttpResponseRedirect(reverse('accounts:fill_driver_details'))
    else:
        form = AccountsForm()
    return render(request, 'create_account.html', {'form':form})

def view_account_details(request, user_name):
    account_info = account.objects.get(user_name=user_name)
    return render(request, 'view_account_details.html', {'account_info' : account_info})

def fill_driver_details(request):
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            driver = form.save(commit=False)
            driver.account = account.objects.get(user_name=request.user.username)
            driver.save()
            return HttpResponseRedirect(reverse('accounts:fill_vehicle_details'))
    else:
        form = DriverForm()

    return render(request,'fill_driver_details.html', {'form':form})

def view_driver_details(request, user_name):
    driver_info = driver.objects.get(user_name=user_name)
    return render(request, 'view_driver_details.html', {'driver_info':driver_info})

def fill_vehicle_details(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.account = account.objects.get(user_name=request.user.username)
            vehicle.save()
            return HttpResponseRedirect(reverse('accounts:account_confirmation'))
    else:
        form = VehicleForm()

    return render(request,'fill_vehicle_details.html', {'form':form})

def view_vehicle_details(request, user_name):
    vehicle_info = vehicle.objects.get(user_name=user_name)
    return render(request, 'view_vehicle_details.html', {'vehicle_info':vehicle_info})

def account_confirmation(request):
    return render(request, 'account_confirmation.html', {})