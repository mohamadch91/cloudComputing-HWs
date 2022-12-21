from django.shortcuts import render
from rest_framework.response import Response
from .serializers import CryptoSerializer
from rest_framework import generics
import requests

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
        'CBAD064B-9F00-4FD3-8C61-8C6E09B9E4B0'}
        response = requests.get(url, headers=headers)
        name=response.json()['name']
        price=response.json()['price_usd']
        return Response({'name': name
        , 'price': price})
            
    