import requests
from celery import shared_task
from .S3_helper import create_image_url
from .models import Advertisement
IMG_KEY="acc_90ccaadfac4bca7"
IMG_SECRET_KEY="daee709507bb27b5756e6dfac46b5222"
IMG_AUTH="Basic YWNjXzkwY2NhYWRmYWM0YmNhNzpkYWVlNzA5NTA3YmIyN2I1NzU2ZTZkZmFjNDZiNTIyMg=="
IMG_ENDPOINT="https://api.imagga.com"
MAILGUN_API_KEY = "95dbfb630c67c77ea3ab2c439bc559b6-2de3d545-d58ccc46"
MAILGUN_DOMAIN = "sandbox094d96c69abf48f980bb338921d399fd.mailgun.org"
#function to send mail to the user
def send_email(message,email):
	return requests.post(
		"https://api.mailgun.net/v3/"+MAILGUN_DOMAIN+"/messages",
		auth=("api", MAILGUN_API_KEY),
		data={"from": "Mohamad Advertisment app <mailgun@"+MAILGUN_DOMAIN+">",
			"to": [email],
			"subject": "Advertisment APP",
			"text": message})

@shared_task
def second_service_task(id, email):
    #get advertisment image from s3
    #send advertisment to second service
    #get response from second service
    #update advertisment state
    ## get advertisment image from s3
    url=create_image_url(id)
    #send image to image processing service
    response = requests.get(
    IMG_ENDPOINT+'/v2/tags?image_url=%s' % url,
            auth=(IMG_KEY, IMG_SECRET_KEY))
    #get the response

    data=response.json()
    
    res=data["result"]["tags"]
    max_confidence=0
    max_tag=""
    #get the tag with the max confidence
    for i in res:
        text=i["tag"]["en"]
        confidence=i["confidence"]
        if(text == "car" or text == "vehicle" ):
            if(confidence>max_confidence):
                max_confidence=confidence
                max_tag=text
    #check if the tag is car or vehicle
    if(max_confidence>30):
        advertisment=Advertisement.objects.get(id=id)
        advertisment.state="accepted"
        advertisment.category=max_tag
        advertisment.save()
        message="Advertisment with id "+str(id)+" is accepted"
        #send mail to the user
        send_email(message, email)
    #if the tag is not car or vehicle
    if(max_confidence<30):
        advertisment=Advertisement.objects.get(id=id)
        advertisment.state="rejected"
        advertisment.save()
        message="Advertisment with id "+str(id)+" is rejected"
        send_email(message, email)
    
    

      

        
        