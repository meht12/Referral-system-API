from django.urls import path
from .views import *

urlpatterns = [
   path('register/', user_registration, name='user_registration'),
    path('details/', user_detail, name='user_detail'),
    path('referrals/', referrals, name='referrals'),
]