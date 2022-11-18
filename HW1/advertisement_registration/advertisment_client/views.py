from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Advertisement
from .serializers import AdvertisementSerializer,AddAdvertismentSerializer
from .S3_uploader import upload_to_server,s3_url
# Create new advertisment API
class AddAddvertismentView(generics.CreateAPIView):
    serializer_class=AddAdvertismentSerializer
    queryset=Advertisement.objects.all()
    def post(self,request):
        #inja dadm be abr arvan
        new_data={
            "description":request.data["description"],
            "email":request.data["email"]
        }
        serialzer=AdvertisementSerializer(data=new_data)
        if(serialzer.is_valid()):
            serialzer.save()
            data=serialzer.data
            add_id=data['id']
            file=request.data['image']
            url=upload_to_server(file,add_id)
            if(url):
                add=Advertisement.objects.get(id=add_id)
                add.image=s3_url()+str(add_id)
                add.save()
                return Response({"message": f"your advertisment submited with id {add_id}"} ,status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "something went wrong"} ,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        # print(serialzer.errors)
        return Response({"message":"Please complete form correctly"},status=status.HTTP_400_BAD_REQUEST)

# Get advertisment with id API
class GetAddvertismentView(generics.RetrieveAPIView):
    serializer_class=AdvertisementSerializer
    queryset=Advertisement.objects.all()
    def get(self,request,id):
        add=get_object_or_404(Advertisement,id=id)
        serialzer=AdvertisementSerializer(add)
        print(serialzer.data)
        data=serialzer.data
        if(data['state']=="accepted"):
            return Response(data,status=status.HTTP_200_OK)
        elif (data['state']=="pending"):
            return Response({"message":"your advertisment is pending"},status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"message":"your advertisment is rejected"},status=status.HTTP_403_FORBIDDEN)

    