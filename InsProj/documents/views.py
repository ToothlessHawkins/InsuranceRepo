from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
# from reportlab.pdfgen import canvas
# from io import BytesIO
import csv
import datetime

from .models import Transaction
from policies.models import Policy
from accounts.models import Account
from make_claims.models import Claims


"""AUTHENTICATION"""
from django.contrib.auth.decorators import user_passes_test
def not_customer(user):
    if user:
        return user.groups.filter(name='Customer').count() > 0
    return False


@user_passes_test(not_customer, login_url='Authenticate:login')
def home(request):
    return render(request, 'documents/home.html', {})

@user_passes_test(not_customer, login_url='Authenticate:login')
def billing_statements(request):
    # yourAccount = Account.objects.get(username=request.user.username)
    yourStatements = Transaction.objects.get(policy=Account.objects.get(username=request.user.username).active_policy)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Billing_Statements.csv"'
    writer = csv.writer(response)
    writer.writerow(['Billing', request.user.username, datetime.date.today])
    writer.writerow(['Date', 'Prior Balance', 'Balance', 'Amount'])
    for payment in yourStatements:
        writer.writerow([payment.date, payment.PriorBalance, payment.NewBalance, payment.Amount])
    return response

@user_passes_test(not_customer, login_url='Authenticate:login')
def claim_details(request):
    # yourAccount = Account.objects.get(username=request.user.username)
    yourClaims = Claims.objects.filter(Policy_Number=Account.objects.get(username=request.user.username).active_policy.number)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Claims_History.csv"'
    writer = csv.writer(response)
    writer.writerow(['Claims', request.user.username, datetime.date.today])
    writer.writerow(['Policy #', "Driver's License Number", 'VIN Number', 'Claim Date', 'Claim ID', 'Claim Resolved', 'Description'])
    # writer.writerow(['Claim Date', 'Claim ID', 'Claim Resolved', 'Description'])
    for claim in yourClaims:
        writer.writerow([claim.Policy_Number, claim.Drivers_Liscene_Number, claim.VIN, claim.Claimed_Date, claim.Claim_Id, claim.Claim_Resolved_Date, claim.Description])
        # writer.writerow([claim.Claimed_Date, claim.Claim_Id, claim.Claim_Resolved_Date, claim.Description])
    return response