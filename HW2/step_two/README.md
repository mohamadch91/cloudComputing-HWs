# Step two

In this step we wiil create a CryptoCurrency market price tracker. We will use redis as a database and python as a programming language.

also we will use docker to run redis and python-Django.

use redis cache to store data and use Django  to get data from API and show it to user.

also use docker Volumes to store data in host machine.

also we  nedd to create config file for redis annd Django.

config file contains : 

- Django server port
- redis keys expire time : default 5 minutes
- CoinAPI API key



## 2.1

First we need to pull redis image and make container from pulled image

```bash
docker pull redis
docker run --name redis -d redis
```

## 2.2
In this step we will create Django project and app and make image from it.
then push this image to docker hub.
### 2.2.1

Create a Django project

```bash
django-admin startproject crypto
```
### 2.2.2

Create a Django app

```bash
cd crypto
python manage.py startapp cryptoApp
```
#### 2.2.2.1 

Create a class in [Views.py](./crypto/cryptoApp/views.py) file
for get data from API and show it to user

and create a [urls.py](./crypto/cryptoApp/urls.py) file for routing

create Serializer class in [serializers.py](./crypto/cryptoApp/serializers.py) file for serialize data

change [settings.py](./crypto/crypto/settings.py) file for add app 

and add [urls.py](./crypto/crypto/urls.py) file for routing



### 2.2.3
Create a requirements.txt

```bash
Django==4.1.4
django-cors-headers==3.13.0
djangorestframework==3.13.1
requests==2.26.0
requests-toolbelt==0.9.1
requests-unixsocket==0.2.0
redis==3.5.3
```


### 2.2.4

Create a Dockerfile in crypto directory
and run Django server

```bash
FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
CMD python manage.py runserver

```

### 2.2.5

Make image from Dockerfile

```bash
docker build -t crypto .
```

### 2.2.6

Push image to docker hub

```bash
docker tag crypto:latest mohamadch91/crypto:latest
docker push mohamadch91/crypto:latest
```

## 2.3




