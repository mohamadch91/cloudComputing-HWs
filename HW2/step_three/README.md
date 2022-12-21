# Step three

In this step we wiil create a CryptoCurrency market price tracker. We will use redis as a database and python as a programming language.

also we will use docker to run redis and python-Django.

use redis cache to store data and use Django  to get data from API and show it to user.

also use docker Volumes to store data in host machine.

also we  nedd to create config file for redis annd Django.

config file contains : 

- Django server port
- redis keys expire time : default 5 minutes
- CoinAPI API key

- [x]