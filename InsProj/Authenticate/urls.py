from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from Authenticate.views import signUp,logIn

app_name='Authenticate'
urlpatterns = [
    url('signup/',signUp,name = 'signup'),
    url('login/',logIn,name='login'),
    path('logout/', auth_views.logout, {'next_page': 'Authenticate:login'}, name='logout'),
]