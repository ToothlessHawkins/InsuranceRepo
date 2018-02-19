from django.conf.urls import url
from django.urls import path
from make_claims.views import create_claim,edit_claim,view_claim,main_claim,view_status

app_name='make_claims'
urlpatterns = [
    url('create/',create_claim,name='create'),
    path('view/<Claim_Id>/',view_claim,name = 'view'),
    path('status/<Claim_Id>/',view_status,name = 'status'),
    path('edit/<Claim_Id>/',edit_claim,name = 'edit'),
    path('claim/page/',main_claim,name = 'claim_page'),
    ]