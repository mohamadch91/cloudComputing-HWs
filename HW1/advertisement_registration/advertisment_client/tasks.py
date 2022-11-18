import string
import requests
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from celery import shared_task
from .S3_helper import create_image_url
IMG_KEY="acc_90ccaadfac4bca7"
IMG_SECRET_KEY="daee709507bb27b5756e6dfac46b5222"
IMG_AUTH="Basic YWNjXzkwY2NhYWRmYWM0YmNhNzpkYWVlNzA5NTA3YmIyN2I1NzU2ZTZkZmFjNDZiNTIyMg=="
IMG_ENDPOINT="https://api.imagga.com"

@shared_task
def second_service_task(id):
    #get advertisment image from s3
    #send advertisment to second service
    #get response from second service
    #update advertisment state
    ## get advertisment image from s3
    url=create_image_url(id)
    response = requests.get(
    IMG_ENDPOINT+'/v2/tags?image_url=%s' % url,
            auth=(IMG_KEY, IMG_SECRET_KEY))
    data=response.json()

        ## send advertisment to second service

        
        