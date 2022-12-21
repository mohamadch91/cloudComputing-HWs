from django.urls import path
from .views import CryptoPriceView

urlpatterns = [
    path('price/', CryptoPriceView.as_view()),
]