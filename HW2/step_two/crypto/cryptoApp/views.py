from django.shortcuts import render
from rest_framework.response import Response
from .serializers import CryptoSerializer
from rest_framework import status

from rest_framework import generics
import requests
from django.conf import settings
from django.core.cache import cache
class CryptoPriceView(generics.CreateAPIView):
    """CryptoPriceView class to get crypto price

    Args:
        generics (class): View support post method
    """
    serializer_class = CryptoSerializer

    def post(self, request):
        """post method to get crypto price

            check for redis cache 

        Args:
            request (request): request object

        Returns:
            Response: Response object
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        crypto_name = serializer.validated_data['crypto_name']
        try:
            has_key_in_cache=cache.has_key(crypto_name)
        except:
            return Response('Can not connect to redis',status=status.HTTP_503_SERVICE_UNAVAILABLE)
            
        if has_key_in_cache :
            response=cache.get(crypto_name)
            response['detail']="Retrieved from Cache"
        else:    
            try:
                url = f'https://rest.coinapi.io/v1/assets/{crypto_name}'
                headers = {'X-CoinAPI-Key' :
                settings.COINAPI_KEY}
                response = requests.get(url, headers=headers).json()[0]
                response['detail']="Retrieved from API"
            except:
                return Response("Cannot coonect to API",status=status.HTTP_504_GATEWAY_TIMEOUT)

        
        user_response={
            'name':response['name'],
            'price':response['price'],
            'detail':response['detai;']
        }
        return Response(user_response,status=status.HTTP_200_OK)

    