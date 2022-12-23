# Docker and kubernetes useful commands

- [Docker and kubernetes useful commands](#docker-and-kubernetes-useful-commands)
  - [Docker](#docker)
    - [Docker build](#docker-build)
    - [Docker tag](#docker-tag)
    - [Docker push](#docker-push)
    - [Docker run](#docker-run)
    - [Docker exec](#docker-exec)
    - [Docker compose](#docker-compose)
      - [Docker compose up](#docker-compose-up)
      - [Docker compose down](#docker-compose-down)
    - [Docker stop](#docker-stop)
    - [Docker rm](#docker-rm)
    - [Docker rmi](#docker-rmi)
    - [Docker logs](#docker-logs)
    - [Docker ps](#docker-ps)
    - [Docker images](#docker-images)
    - [Docker network](#docker-network)
    - [Docker network create](#docker-network-create)
    - [Docker network connect](#docker-network-connect)
    - [Docker network disconnect](#docker-network-disconnect)
    - [Docker network rm](#docker-network-rm)
    - [Docker volume](#docker-volume)
    - [Docker volume create](#docker-volume-create)
    - [Docker volume rm](#docker-volume-rm)
    - [Docker volume inspect](#docker-volume-inspect)
    - [Docker volume prune](#docker-volume-prune)
  - [Kubernetes](#kubernetes)
    - [Minikube start](#minikube-start)
    - [Kubectl create](#kubectl-create)
    - [Kubectl apply](#kubectl-apply)
    - [Kubectl edit](#kubectl-edit)
    - [Kubectl rollout](#kubectl-rollout)
    - [Kubectl delete](#kubectl-delete)
    - [Kubectl get](#kubectl-get)
      - [example](#example)
    - [Kubectl describe](#kubectl-describe)
      - [example](#example-1)
    - [Kubectl logs](#kubectl-logs)
    - [Kubectl exec](#kubectl-exec)
    - [Kubectl run](#kubectl-run)
    - [Kubectl expose](#kubectl-expose)
    - [Kubectl port-forward](#kubectl-port-forward)



## Docker

### Docker build

This command is used to build a docker image from a dockerfile

```bash
docker build -t <image_name> <path_to_dockerfile>
```

### Docker tag

This command is used to tag a docker image

```bash
docker tag <image_name> <new_image_name>
```

### Docker push

This command is used to push a docker image to docker hub

```bash
docker push <image_name>
```

### Docker run

This command is used to run a docker image as a container

```bash
docker run -d -p <host_port>:<container_port> <image_name>
```

you can use the -v flag to mount a volume to the container

```bash
docker run -d -p <host_port>:<container_port> -v <host_path>:<container_path> <image_name>
```

also you can use the -e flag to set environment variables

```bash
docker run -d -p <host_port>:<container_port> -e <env_var_name>=<env_var_value> <image_name>
```

and you can use the --name flag to set a name for the container

```bash
docker run -d -p <host_port>:<container_port> --name <container_name> <image_name>
```

--network flag is used to set the network of the container

```bash
docker run -d -p <host_port>:<container_port> --network <network_name> <image_name>
```

**Complete run command**

```bash
docker run -d -p -it <host_port>:<container_port> -v <host_path>:<container_path> -e <env_var_name>=<env_var_value> --name <container_name> --network <network_name> <image_name>
```

### Docker exec

This command is used to execute a command in a running container

```bash
docker exec -it <container_name> <command>
```
### Docker compose

#### Docker compose up
This command is used to run a docker-compose file

```bash
docker compose up -d
```

#### Docker compose down

This command is used to stop and remove a docker-compose file

```bash
docker compose down
```






### Docker stop

This command is used to stop a running container

```bash
docker stop <container_name>
```

### Docker rm

This command is used to remove a container

```bash
docker rm <container_name>
```

### Docker rmi

This command is used to remove a docker image

```bash
docker rmi <image_name>
```

### Docker logs

This command is used to see the logs of a container

```bash
docker logs <container_name>
```

### Docker ps

This command is used to see the running containers

```bash
docker ps
```

### Docker images

This command is used to see the docker images

```bash
docker images
```

### Docker network

This command is used to see the docker networks

```bash
docker network ls
```

### Docker network create

This command is used to create a docker network

```bash
docker network create <network_name>
```

### Docker network connect

This command is used to connect a container to a network

```bash
docker network connect <network_name> <container_name>
```

### Docker network disconnect

This command is used to disconnect a container from a network

```bash

docker network disconnect <network_name> <container_name>
```

### Docker network rm

This command is used to remove a docker network

```bash
docker network rm <network_name>
```

### Docker volume

This command is used to see the docker volumes

```bash
docker volume ls
```

### Docker volume create

This command is used to create a docker volume

```bash
docker volume create <volume_name>
```

### Docker volume rm

This command is used to remove a docker volume

```bash
docker volume rm <volume_name>
```

### Docker volume inspect

This command is used to inspect a docker volume

```bash
docker volume inspect <volume_name>
```

### Docker volume prune

This command is used to remove all unused volumes

```bash
docker volume prune
```

## Kubernetes

if you want to use kubernetes commands you should install kubectl

or you can use minikube to run a local kubernetes cluster

### Minikube start

This command is used to start a local kubernetes cluster

```bash
minikube start
```

### Kubectl create

This command is used to create a kubernetes manifest file

```bash
kubectl create deployment <deployment_name> --image=<image_name> --dry-run=client -o yaml > <manifest_file_path>
```

or with minikube

```bash

minikube kubectl -- create deployment <deployment_name> --image=<image_name> --dry-run=client -o yaml > <manifest_file_path>
```


### Kubectl apply

This command is used to apply a kubernetes manifest file

```bash
kubectl apply -f <manifest_file_path>
```
or with minikube
```bash
minikube kubectl -- apply -f <manifest_file_path>
```

### Kubectl edit

This command is used to edit a kubernetes manifest file

```bash
kubectl edit -f <manifest_file_path>
```
or with minikube

```bash
minikube kubectl -- edit -f <manifest_file_path>
```

###  Kubectl rollout

This command is used to rollout a kubernetes manifest file

```bash

kubectl rollout restart -f <manifest_file_path>
```

or with minikube

```bash

minikube kubectl -- rollout restart -f <manifest_file_path>
```

you can rollout a deployment with the following command

```bash
kubectl rollout restart deployment <deployment_name>
```

or with minikube

```bash
minikube kubectl -- rollout restart deployment <deployment_name>
```




### Kubectl delete

This command is used to delete a kubernetes manifest file

```bash
kubectl delete -f <manifest_file_path>
```

or with minikube

```bash
minikube kubectl -- delete -f <manifest_file_path>
```

### Kubectl get

This command is used to get a kubernetes resource

```bash
kubectl get <resource_name>
```
or with minikube

```bash
minikube kubectl -- get <resource_name>
```


#### example

```bash
kubectl get pods
```

### Kubectl describe

This command is used to describe a kubernetes resource

```bash
kubectl describe <resource_name>
```
or with minikube

```bash
minikube kubectl -- describe <resource_name>
```

#### example

```bash
kubectl describe pod <pod_name>
```

### Kubectl logs

This command is used to see the logs of a pod

```bash
kubectl logs <pod_name>
```
or with minikube

```bash
minikube kubectl -- logs <pod_name>
```

### Kubectl exec

This command is used to execute a command in a pod

```bash
kubectl exec -it <pod_name> <command>
```
or with minikube

```bash
minikube kubectl -- exec -it <pod_name> <command>
```

### Kubectl run

This command is used to run a container as a pod

```bash
kubectl run <pod_name> --image=<image_name>

```

or with minikube

```bash
minikube kubectl -- run <pod_name> --image=<image_name>
```

### Kubectl expose

This command is used to expose a pod as a service

```bash
kubectl expose pod <pod_name> --port=<port> --type=<type>
```

or with minikube

```bash
minikube kubectl -- expose pod <pod_name> --port=<port> --type=<type>
```

### Kubectl port-forward

This command is used to forward a port from a pod to the host

```bash
kubectl port-forward <pod_name> <host_port>:<container_port>
```

or with minikube

```bash
minikube kubectl -- port-forward <pod_name> <host_port>:<container_port>
```





