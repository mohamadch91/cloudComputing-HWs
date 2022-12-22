# Step four

In this step we will run first app in a kubernetes cluster.
and request with curl to get btc data.

## 4.1 run app in kubernetes cluster

```bash
minikube kubectl -- run curl --image=mohamadch91/curl --restart=Never --command -- curl http://crypto:8000/btc
```

## 4.2 check result

```bash
minikube kubectl -- get pods
```

then 

```bash
kubectl logs ${POD_NAME} ${CONTAINER_NAME}

```