# Step one

In this step we will create a simple Docker image that will contain a CURL command to send a request to the google.com website.

## 1.1

first we need too create Dockerfile with alpine base image and install curl package.

```Dockerfile
FROM alpine:latest
RUN apk add --update curl
ENTRYPOINT ["curl"]
```

