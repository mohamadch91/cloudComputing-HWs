from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Advertisement
from .serializers import AdvertisementSerializer,AddAdvertismentSerializer
from .S3_helper import upload_to_server,s3_url
import requests
from .tasks import second_service_task
# Create new advertisment API

class AddAddvertismentView(generics.CreateAPIView):
    serializer_class=AddAdvertismentSerializer
    queryset=Advertisement.objects.all()
    #define the post method
    def post(self,request):
        #get the data from the request
        new_data={
            "description":request.data["description"],
            "email":request.data["email"]
        }
        #create the serializer
        serialzer=AdvertisementSerializer(data=new_data)
        #check if the data is valid
        if(serialzer.is_valid()):
            #save the data
            serialzer.save()
            data=serialzer.data
            #upload the image to the server
            add_id=data['id']
            file=request.data['image']
            url=upload_to_server(file,add_id)
            #update the url in the database
            if(url):
                add=Advertisement.objects.get(id=add_id)
                add.image=s3_url()+str(add_id)+".jpg"
                add.save()
                #call the second service from celery
                second_service_task.delay(add_id)
                #return the response
                return Response({"message": f"your advertisment submited with id {add_id}"} ,status=status.HTTP_201_CREATED)
            #if the image is not uploaded
            else:
                return Response({"message": "something went wrong"} ,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        #if the data is not valid
        return Response({"message":"Please complete form correctly"},status=status.HTTP_400_BAD_REQUEST)

#Get advertisment with id API
#class for get advertisment with id
class GetAddvertismentView(generics.RetrieveAPIView):

    serializer_class=AdvertisementSerializer
    queryset=Advertisement.objects.all()
    #define the get method
    def get(self,request,id):
        #get the advertisment with the id
        add=get_object_or_404(Advertisement,id=id)
        serialzer=AdvertisementSerializer(add)
        data=serialzer.data
        #check if the advertisment is approved
        if(data['state']=="accepted"):
            return Response(data,status=status.HTTP_200_OK)
        elif (data['state']=="pending"):
            return Response({"message":"your advertisment is pending"},status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"message":"your advertisment is rejected"},status=status.HTTP_403_FORBIDDEN)

    