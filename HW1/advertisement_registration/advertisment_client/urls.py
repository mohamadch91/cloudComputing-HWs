from django.urls import path
from .views import *


urlpatterns = [

    path('add', AddAddvertismentView.as_view(), name='add advertisment'),
    path('get/<int:id>', GetAddvertismentView.as_view(), name='get advertisment'),
    
    
]