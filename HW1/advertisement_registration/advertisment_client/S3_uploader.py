import boto3
import logging
from botocore.exceptions import ClientError

# Configure logging
logging.basicConfig(level=logging.INFO)

try:
    s3_resource = boto3.resource(
        's3',
        endpoint_url='endpoint_url',
        aws_access_key_id='access_key',
        aws_secret_access_key='secret_key'
    )

except Exception as exc:
    logging.error(exc)
else:
    try:
        bucket = s3_resource.Bucket('bucket-name')
        file_path = 'the/abs/path/to/file.txt'
        object_name = 'file.txt'

        with open(file_path, "rb") as file:
            bucket.put_object(
                ACL='private',
                Body=file,
                Key=object_name
            )
    except ClientError as e:
        logging.error(e)
