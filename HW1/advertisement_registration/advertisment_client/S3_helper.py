import boto3
import logging
from botocore.exceptions import ClientError

# Configure logging
def upload_to_server(file,id):
    logging.basicConfig(level=logging.INFO)

    try:
        s3_resource = boto3.resource(
            's3',
            endpoint_url='https://s3.ir-thr-at1.arvanstorage.com',
            aws_access_key_id='57cbf04d-38dc-4ab4-817a-7f232aead7f1',
            aws_secret_access_key='4758e835ebedf4818de354c5db7b35c979b100b9'
        )

    except Exception as exc:
        print("inja")
        logging.error(exc)
    else:
        try:
            bucket = s3_resource.Bucket('cloud-hw')
            bucket.put_object(
                    ACL='public-read',
                    Body=file,
                    Key=str(id)+".jpg",
                )
            return True
        except ClientError as e:
            print("na innja")
            logging.error(e)

def s3_url():
    return "https://cloud-hw.s3.ir-thr-at1.arvanstorage.com/"

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
