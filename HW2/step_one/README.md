# Step one

In this step we will create a simple Docker image that will contain a CURL command to send a request to the google.com website.
then we will upload the image to the docker hub.
pull  the image from the docker hub and create container from it.

run the container and send a request to the google.com website.


## 1.1

first we need too create Dockerfile with alpine base image and install curl package.

```Dockerfile
FROM alpine:latest
RUN apk add --update curl
ENTRYPOINT ["curl"]
```

## 1.2

now we need to push the image to the docker hub.

```bash
docker build -t curl .
docker tag curl:latest <dockerhub_username>/curl:latest
docker push <dockerhub_username>/curl:latest
```