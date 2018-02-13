from django.shortcuts import render,redirect
from django.urls import reverse
from Authenticate.forms import SignUpFOrm,LoginForm
from django.contrib.auth import authenticate,login
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import Group,Permission, User

customer_group,created = Group.objects.get_or_create(name = 'Customer')
# Create your views here.

def signUp(request):
    if request.method == 'POST':
        form = SignUpFOrm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            pword = form.cleaned_data.get('password1')
            user = authenticate(user_name =username,password = pword )
            myuser = User.objects.get(username=username)
            myuser.groups.add(customer_group)
            login(request,user)
            return HttpResponse("Welcome")

    else:
        form = SignUpFOrm()
        return render(request,'Authenticate/sign_up.html',{'form':form})

def logIn(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username,password = password)
            if user is not None:
                login(request,user)
                if user.groups.filter(name='Customer').exists():
                    return HttpResponse('see your payments')
                elif user.groups.filter(name='Adjuster').exists():
                    return HttpResponseRedirect(reverse('adjusters:home'))
                elif user.groups.filter(name='ServiceRep').exists():
                    return HttpResponseRedirect(reverse('service:home'))
                else:
                    return HttpResponse('This user is not associated with a group (Customer, Adjuster, or ServiceRep).')
            else:
                return HttpResponse('given credentials doesn\'t match.please enter valid credentials.')

    else:
        form = LoginForm()
        return render(request,'Authenticate/log_in.html',{'form':form})