import boto3
import logging
from botocore.exceptions import ClientError
ENDPOINT_URL = "https://s3.ir-thr-at1.arvanstorage.com"
ACCESS_KEY='57cbf04d-38dc-4ab4-817a-7f232aead7f1'
SECRET_KEY='4758e835ebedf4818de354c5db7b35c979b100b9'
BUCKET_NAME = 'cloud-hw'
# Configure logging
#function to upload file to s3
def upload_to_server(file,id):
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
                    Body=file,
                    Key=str(id)+".jpg",
                )
            return True
        except ClientError as e:
            logging.error(e)


#function to get the s3 url of the file
def create_image_url(id):
    return "https://cloud-hw.s3.ir-thr-at1.arvanstorage.com/"+str(id)+".jpg"

def download_from_server(id):
    logging.basicConfig(level=logging.INFO)

    try:
        s3_resource = boto3.resource(
            's3',
            endpoint_url='https://s3.ir-thr-at1.arvanstorage.com',
            aws_access_key_id='57cbf04d-38dc-4ab4-817a-7f232aead7f1',
            aws_secret_access_key='4758e835ebedf4818de354c5db7b35c979b100b9'
        )
    except Exception as exc:
        logging.error(exc)
    else:
        try:
            bucket = s3_resource.Bucket('cloud-hw')
            download_path = '/tmp/{}{}'.format(id, '.jpg')
            bucket.download_file(str(id)+".jpg", download_path)
            return True
        except ClientError as e:
            logging.error(e)
