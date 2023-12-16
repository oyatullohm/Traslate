from django.urls import path

from . views import *
from . ajax import *
urlpatterns = [
    path('',index) ,
    path('trans', trans) ,
    path ('api',transApi),
    
    ]