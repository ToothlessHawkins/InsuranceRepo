from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
# from reportlab.pdfgen import canvas
# from io import BytesIO
import csv
import datetime

from .models import Transaction
"""IMPORT MODELs FROM APPs HERE"""
# from policies.models import Policy
# from accounts.models import Account
from make_claims.models import Claims

def home(request):
    return render(request, 'documents/home.html', {})

def billing_statements(request):
    """SWITCH THESE TO BE USER SPECIFIC"""
    # yourAccount = Account.objects.get(username=request.user.username)
    # yourStatements = Transaction.objects.get(policy=yourAccount.active_policy)
    yourStatements = Transaction.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Billing_Statements.csv"'
    writer = csv.writer(response)
    # writer.writerow(['Billing', request.user.username, datetime.date.today])
    writer.writerow(['Date', 'Prior Balance', 'Balance', 'Amount'])
    for payment in yourStatements:
        writer.writerow([payment.date, payment.PriorBalance, payment.NewBalance, payment.Amount])
    return response

def claim_details(request):
    """SWITCH THESE TO BE USER SPECIFIC"""
    # yourAccount = Account.objects.get(username=request.user.username)
    # yourClaims = Claims.objects.filter(Policy_Number=yourAccount.active_policy.number)
    yourClaims = Claims.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Claims_History.csv"'
    writer = csv.writer(response)
    # writer.writerow(['Claims', request.user.username, datetime.date.today])
    # writer.writerow(['Policy #', "Driver's License Number", 'VIN Number', 'Claim Date', 'Claim ID', 'Claim Resolved', 'Description'])
    writer.writerow(['Claim Date', 'Claim ID', 'Claim Resolved', 'Description'])
    for claim in yourClaims:
        # writer.writerow([claim.Policy_Number, claim.Drivers_Liscene_Number, claim.VIN, claim.Claimed_Date, claim.Claim_Id, claim.Claim_Resolved_Date, claim.Description])
        writer.writerow([claim.Claimed_Date, claim.Claim_Id, claim.Claim_Resolved_Date, claim.Description])
    return response