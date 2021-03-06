from django.shortcuts import render,redirect
from Discounts.models import Disconts_table,Customer_Spcific_Discounts,General_Discounts
from Discounts.forms import General_Disounts_Form,Discount_Table_Form
from policies.models import policy
from django.contrib.auth.models import User
from accounts.models import account
# Create your views here.
import string
import random
def view_general_discounts(request):
    g_d = General_Discounts.objects.all()
    return render(request,'Discounts/view_general_discounts.html',{'discounts':g_d})

def view_customer_specific_discounts(request):
    crnt_user = User.objects.get(username=request.user.username)
    user = account.objects.get(user_name=crnt_user)
    if crnt_user.groups.filter(name='Customer').exists():
        p_i = policy.objects.get(account = user)
    #c_d = Customer_Spcific_Discounts.objects.get(Policy_Id = p_i)
        p_r = Disconts_table.objects.filter(points_required__lte = p_i.points)
        return render(request,'Discounts/customer_specific.html',{'discounts':p_r,'points':p_i})

def create_general_discounts(request):
    cupcode = ''.join([random.choice(string.ascii_uppercase+string.digits) for i in range(5)])
    if request.method == 'POST':
        form = General_Disounts_Form(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.Cupon_Code = cupcode
            temp.save()
            return redirect('Discounts:creategeneraldiscounts')

    else:
        form = General_Disounts_Form()
        return render(request,'Discounts/create_general_disccounts.html',{'form':form})


def create_customer_discounts(request):
    cupcode = ''.join([random.choice(string.ascii_uppercase + string.digits+string.ascii_lowercase) for i in range(5)])
    if request.method == 'POST':
        form = Discount_Table_Form(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.Cupon_Code = cupcode
            temp.save()
            return redirect('Discounts:createcustomerdiscounts')

    else:
        form = Discount_Table_Form()
        return render(request, 'Discounts/create_customer_discounts.html', {'form': form})

def all_discounts(request):
    return render(request,'Discounts/all_discounts.html',{})