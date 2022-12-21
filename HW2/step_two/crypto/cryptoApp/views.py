from django.shortcuts import render
from rest_framework.response import Response
from .serializers import CryptoSerializer
from rest_framework import generics
import requests

import crypto.settings as settings

class CryptoPriceView(generics.CreateAPIView):
    """CryptoPriceView class to get crypto price

    Args:
        generics (class): View support post method
    """
    serializer_class = CryptoSerializer

    def post(self, request):
        """post method to get crypto price

        Args:
            request (request): request object

        Returns:
            Response: Response object
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        crypto_name = serializer.validated_data['crypto_name']
        url = f'https://rest.coinapi.io/v1/assets/{crypto_name}'
        headers = {'X-CoinAPI-Key' :
        settings.COIN_API_KEY}
        response = requests.get(url, headers=headers).json()[0]
        name=response['name']
        price=response['price_usd']
        return Response({'name': name
        , 'price': price})

    