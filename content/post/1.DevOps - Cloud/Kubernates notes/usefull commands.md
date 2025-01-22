```
minikube image load full-frontend:latest
```

```
minikube image load full-backend:latest
```

```
minikube image list
```

```
eval $(minikube docker-env)
docker images
```

```
eval $(minikube docker-env --unset)
```

```
kubectl apply -f .
```
kubectl delete -f .
```