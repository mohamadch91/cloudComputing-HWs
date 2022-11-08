from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Advertisement
from .serializers import AdvertisementSerializer

# Create new advertisment API
class AddAddvertismentView(generics.CreateAPIView):
    serializer_class=AdvertisementSerializer
    queryset=Advertisement.objects.all()
    def post(self,request):
        serialzer=AdvertisementSerializer(data=request.data)
        if(serialzer.is_valid()):
            serialzer.save()
            data=serialzer.data
            add_id=data['id']
            return Response({"message": f"your advertisment submited with id {add_id}"} ,status=status.HTTP_201_CREATED)
        return Response({"message":"Please complete form correctly"},status=status.HTTP_400_BAD_REQUEST)
