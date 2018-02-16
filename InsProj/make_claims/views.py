from django.shortcuts import render
from make_claims.forms import ClaimForm
import string
import random
from django.http import HttpResponse
from make_claims.models import Claims
from django.contrib.auth.models import User
from accounts.models import account
from policies.models import policy




# Create your views here.


def create_claim(request):
    c_id = ''.join([random.choice(string.ascii_uppercase + string.digits) for n in range(9)])
    if request.method == 'POST':
        claim_data = ClaimForm(request.POST)
        if claim_data.is_valid():
            data = claim_data.save(commit=False)
            data.Claim_Id = c_id
            data.save()
            return HttpResponse("Your claim is created.\nYour claim ID is: {}".format(data.Claim_Id))
    else:
        claim_data = ClaimForm()
        return render(request,'claims/creating_claim.html',{'claim':claim_data})

def view_claim(request,Claim_Id):
    if request.method == 'GET':
        claim = Claims.objects.get(Claim_Id=Claim_Id)
        return render(request,'claims/viewclaim.html',{'claim':claim})

def edit_claim(request,Claim_Id):
    claim = Claims.objects.get(Claim_Id=Claim_Id)
    claim_data = ClaimForm(request.POST,instance=claim)
    if claim_data.is_valid():
        claim_data.save()
        return HttpResponse("your claim is updated")
    else:
        claim_data = ClaimForm(instance=claim)
        return render(request,'claims/editclaim.html',{'claim':claim_data})

def main_claim(request):
    user = User.objects.get(username=request.user.username)
    if user.groups.filter(name='Customer').exists():
        user_policy = policy.objects.get(user_name=account.objects.get(user_name=user))
        claim_obj = Claims.objects.filter(Policy= user_policy)
    #claim_obj = Claims.objects.all()
        return render(request,'claims/claim_page.html',{'claim_id':claim_obj})

def view_status(request,Claim_Id):
    claim_staus = Claims.objects.get(Claim_Id=Claim_Id)
    status =claim_staus.Status
    return render(request,'claims/viewstatus.html',{'status':status})


