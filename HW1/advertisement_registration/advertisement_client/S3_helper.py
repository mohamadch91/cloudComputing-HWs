import boto3
import logging
from botocore.exceptions import ClientError
ENDPOINT_URL = "https://s3.ir-thr-at1.arvanstorage.com"
ACCESS_KEY='57cbf04d-38dc-4ab4-817a-7f232aead7f1'
SECRET_KEY='4758e835ebedf4818de354c5db7b35c979b100b9'
BUCKET_NAME = 'cloud-hw'
# Configure logging
#function to upload file to s3
def upload_to_server(image_file,addvertisment_id):
    logging.basicConfig(level=logging.INFO)
    #define the s3 resource
    try:
        s3_resource = boto3.resource(
            's3',
            endpoint_url=ENDPOINT_URL,
            aws_access_key_id=ACCESS_KEY,
            aws_secret_access_key=SECRET_KEY
        )

    except Exception as exc:
        logging.error(exc)
    else:
        try:
            #upload the file to s3
            bucket = s3_resource.Bucket(BUCKET_NAME)
            bucket.put_object(
                    ACL='public-read',
                    Body=image_file,
                    Key=str(addvertisment_id)+".jpg",
                )
            return True
        except ClientError as e:
            logging.error(e)


#function to get the s3 url of the file
def create_image_url(addvertisment_id):
    return "https://cloud-hw.s3.ir-thr-at1.arvanstorage.com/"+str(addvertisment_id)+".jpg"

#function to download the file from s3
#if you want to download the file from s3 you can use this function
#please note that you should have the file in your s3 bucket
#and you should have the id of the file
#the function will download the file in the /tmp directory
#you can change the download path
#the function will return True if the file is downloaded
#and False if the file is not downloaded
#uncomment the function to use it
# def download_from_server(addvertisment_id):
#     logging.basicConfig(level=logging.INFO)

#     try:
#         s3_resource = boto3.resource(
#             's3',
#             endpoint_url='https://s3.ir-thr-at1.arvanstorage.com',
#             aws_access_key_id='57cbf04d-38dc-4ab4-817a-7f232aead7f1',
#             aws_secret_access_key='4758e835ebedf4818de354c5db7b35c979b100b9'
#         )
#     except Exception as exc:
#         logging.error(exc)
#     else:
#         try:
#             bucket = s3_resource.Bucket('cloud-hw')
#             download_path = '/tmp/{}{}'.format(addvertisment_id, '.jpg')
#             bucket.download_file(create_image_url(addvertisment_id), download_path)
#             return True
#         except ClientError as e:
#             logging.error(e)
#             return False
