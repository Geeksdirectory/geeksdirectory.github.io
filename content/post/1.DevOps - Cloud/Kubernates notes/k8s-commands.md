---
title: Kubernates notes usefull commands
date: 2025-01-22
---


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

```
kubectl delete -f .
```

```
kubectl apply -f kube
```

```
minikube service knote --url
```

```
kubectl scale --replicas=2 deployment/knote
```


lens-ui 
mantis 

```
kubectl autoscale deployment knote --cpu-percent=50 --min=1 --max=5
````

```
kubectl get hpa
```

```
kubectl get pods -w
```

```
kubectl get pods -o wide
```

kubectl delete -f kube
```


# switch namespaces

```
kubectl config set-context --current --namespace=argocd



## create nginx pod 

```
kubectl run myapp-pod --image=nginx --restart=Never
```


```
kubectl delete pod webapp
```


scale replicas
```
kubectl scale --replicas=6 -f replicaset-defination.yml
```


![[Pasted image 20250217123143.png]]