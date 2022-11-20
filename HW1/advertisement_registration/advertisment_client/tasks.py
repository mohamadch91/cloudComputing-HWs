import requests
from celery import shared_task
from .S3_helper import create_image_url
from .models import Advertisement
IMG_KEY="acc_90ccaadfac4bca7"
IMG_SECRET_KEY="daee709507bb27b5756e6dfac46b5222"
IMG_AUTH="Basic YWNjXzkwY2NhYWRmYWM0YmNhNzpkYWVlNzA5NTA3YmIyN2I1NzU2ZTZkZmFjNDZiNTIyMg=="
IMG_ENDPOINT="https://api.imagga.com"
#function to send mail to the user
def send_simple_message(message):
	return requests.post(
		"https://api.mailgun.net/v3/sandbox094d96c69abf48f980bb338921d399fd.mailgun.org/messages",
		auth=("api", "95dbfb630c67c77ea3ab2c439bc559b6-2de3d545-d58ccc46"),
		data={"from": "Excited User <mailgun@sandbox094d96c69abf48f980bb338921d399fd.mailgun.org>",
			"to": ["mohamadchoupan80@gmail.com","mohamadchoupan94@gmail.com"],
			"subject": "Advertisment APP",
			"text": message})

@shared_task
def second_service_task(id):
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
        if(text == "car" or text == "vehicle" or text == "transportation" or text == "automobile" or text == "motor vehicle" or text == "motorcar" or text == "machine" or text == "motor" or text == "motorcycle" or text == "motorbike"):
            if(confidence>max_confidence):
                max_confidence=confidence
                max_tag=text
    #check if the tag is car or vehicle
    if(max_confidence>0):
        advertisment=Advertisement.objects.get(id=id)
        advertisment.state="accepted"
        advertisment.category=max_tag
        advertisment.save()
        message="Advertisment with id "+str(id)+" is accepted"
        #send mail to the user
        send_simple_message(message)
    #if the tag is not car or vehicle
    if(max_confidence==0):
        advertisment=Advertisement.objects.get(id=id)
        advertisment.state="rejected"
        advertisment.save()
        message="Advertisment with id "+str(id)+" is rejected"
        send_simple_message(message)
    
    

      

        
        