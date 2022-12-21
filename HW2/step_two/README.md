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
then 
Create a Django project

```bash
django-admin startproject crypto
```

### 2.2.1

Create a Django app

```bash
cd crypto
python manage.py startapp crypto
```






