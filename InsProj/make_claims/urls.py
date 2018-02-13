from django.conf.urls import url
from django.urls import path
from make_claims.views import create_claim,edit_claim,view_claim
app_name='make_claims'
urlpatterns = [
    url('create/',create_claim,name='create'),
    path('view/<Claim_Id>/',view_claim,name = 'view'),
    path('edit/<Claim_Id>/',edit_claim,name = 'edit')
]