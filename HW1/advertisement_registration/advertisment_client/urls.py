from django.urls import path
from .views import *


urlpatterns = [

    path('add', AddAddvertismentView.as_view(), name='add advertisment'),
    
    
]