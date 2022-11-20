# Cloud computing Course from AUT 
# Home work1 
to see project description please read CC-HW1.pdf
## 1.1
we have one Django project with one app in it.
to run the project please use the following command:
```
    cd HW1/advertisment_registration
    python manage.py runserver
```
and in the sprate terminal run the following command:
```
    cd HW1/advertisment_registration
    celery -A advertisement_registration  worker -l info
```

Service is running on port 8000.
you can open the following link to see the service:
on your local machine:
1. Add new advertisment: 
    1. [Add new advertisement](http://localhost:8000/advertisment/add)
    2. [Get advertisement with id](http://localhost:8000/advertisment/get/1)
## 1.2
### We use 5 cloud services in this project:
1. S3 for storing static files
    use   [Abrarvan S3 bucket](https://www.arvancloud.com/fa)
if you want to use your own bucket please change the following line in advertisement_client/S3_helper.py:
```
    ENDPOINT_URL = "https://s3.ir-thr-at1.arvanstorage.com"
    ACCESS_KEY='Your Acces Key'
    SECRET_KEY='Your Secret Key'
    BUCKET_NAME = 'Your Bucket Name'
```
2. Postgres for database (DbaaS)
    use [runflare](https://runflare.com/) Postgres database
if you want to use your own database please change the following line in settings.py:
```
    DATABASES = {
  'default': {
     'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db name',
        'USER': 'user name',
        'PASSWORD': 'password',
        'HOST': 'DB host',
        'PORT': 'DB port',
}
}
```
3. RabbitMQ for message queue
    use [CloudAMPQ](https://www.cloudamqp.com/) RabbitMQ
if you want to use your own RabbitMQ please change the following line in settings.py:
```
    CELERY_BROKER_URL = 'Your CloudAMPQ URL'
```
4. Image processing service
    use [Imagga](https://imagga.com/) image processing service
if you want to use your own image processing service please change the following line in advertisement_client/tasks.py:
```
    IMG_KEY="Your Imagga Key"
    IMG_SECRET_KEY="Your Imagga Secret Key"
    IMG_AUTH="Your Image Auth"
    IMG_ENDPOINT="https://api.imagga.com"

```
5. Email service
    use [Mailgun](https://www.mailgun.com/) email service
if you want to use your own email service please change the following line in advertisement_client/tasks.py:
```
    MAILGUN_API_KEY = "Your Mailgun API Key"
    MAILGUN_DOMAIN = "Your Mailgun Domain"
```
## 1.3
### How to use the project:
1. First you need to run  the project.
2. Then you can open the [this link](http://localhost:8000/advertisment/add) to see the service

3. You can add a new advertisment by filling the form and click on submit button.
4. After submitting the form you will see the advertisment id.
5. You can open the [this link](http://localhost:8000/advertisment/get/1) to see the advertisment details:
6. You can see the advertisment details and the image tags.

## 1.4
### Code structure:
1. advertisment_registration: Django project
2. advertisement_client: Django app
3. advertisement_client/models.py: contains the Advertisment model class  contains the following fields:
    1. title: CharField
    2. description: TextField
    3. image: CharField
    4. email: EmailField
    5. state: CharField
    6. category: CharField
4. advertisement_client/views.py: contains the views of the project and the following functions:
    1. add_advertisment: AddAddvertismentView inheits from generics.CreateAPIView:
        1. post: add advertisment to the database and send the advertisment id to the user
            also  send the advertisment image to S3 and send the image to image processing service
            and email the advertisment image status to the user
    2. get_advertisment: GetAddvertismentView enherits from generics.RetrieveAPIView: 
        1. get: get advertisment from the database and send the advertisment details to the user
5. advertisement_client/urls.py: contains the urls of the project
6. advertisement_client/serializers.py: contains the serializers of the project
7. advertisement_client/tasks.py: contains the tasks of the project must be run in the background
    1. second_service_task function:
        1. retrieve image url from S3
        2. send_image_to_imagga: send the advertisment image to image processing service
        3. send_email: send_email
            1. send_email: send email to the user with mailgun
8. advertisement_client/S3_helper.py: contains the S3 helper functions
    1. upload_to_server: upload the advertisment image to S3
    2. download_from_server: get the advertisment image from S3 you need to uncomment the following line in S3_helper.py:
        ```
        # download_from_server(image_id)
        ...
        ```
    3. create_image_url: create the advertisment image url

