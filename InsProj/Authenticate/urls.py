from django.conf.urls import url
from django.urls import path
from Authenticate.views import signUp,logIn


urlpatterns = [
    url('signup/',signUp,name = 'signup'),
    url('login/',logIn,name='login')
]