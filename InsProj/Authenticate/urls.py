from django.conf.urls import url
from django.urls import path
from Authenticate.views import signUp,logIn

app_name='Authenticate'
urlpatterns = [
    url('signup/',signUp,name = 'signup'),
    url('login/',logIn,name='login')
]