## Home work 2

# Docker and Kubernetes

## Project description
to see the project description please visit the following link:

- [Step one](./step_one/)
- [Step two](./step_two/)
- [Step three](./step_three/)
- [Step four](./step_four/)



## Tools

for this Project we will use the following tools:
- Docker
- Kubernetes
- Redis
- Django
- Docker-compose


## Docker

### Dockerfile

The Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image. Using docker build users can create an automated build that executes several command-line instructions in succession.

### Docker-compose

Docker Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration.

## Kubernetes

### Pods

A Pod is a Kubernetes abstraction that represents a group of one or more application containers (such as Docker or rkt), and some shared resources for those containers. Those resources include:

Shared storage, as Volumes
Networking, as a unique cluster IP address
Information about how to run each container, such as the container image version or specific ports to use

### Services

A Kubernetes Service is an abstraction which defines a logical set of Pods and a policy by which to access them - sometimes called a micro-service. The set of Pods targeted by a Service is (usually) determined by a Label Selector (see below for why you might want a Service without including Pods in the set).

### Deployments

A Deployment provides declarative updates for Pods and ReplicaSets.

### Ingress

An Ingress is a collection of rules that allow inbound connections to reach the cluster services.

## Redis

Redis is an open source (BSD licensed), in-memory data structure store, used as a database, cache and message broker. It supports data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs, geospatial indexes with radius queries and streams.

## Django

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.
