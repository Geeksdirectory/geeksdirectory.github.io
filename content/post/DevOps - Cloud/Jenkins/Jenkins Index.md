
## Setting up jenkins using Docker

```
docker pull jenkins/jenkins:lts
```


Create a network for Jenkins if you plan to connect it with other services (e.g., Docker agents or a database):

```
docker network create jenkins
```
