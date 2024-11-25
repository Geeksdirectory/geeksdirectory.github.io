 ```
docker build -t myimage . 
```


docker run -d -p 5173:5173 -v /home/yash/Desktop/obsidiangraph/graphnotes:/app --name oopsidian oopsidian


to run docker container in specific port and allocate volume to it and also name it 
command :

```
docker run -d -p 8080:9000 -v /host/volume:/containervolume --name container_name image
```


command to access the container's shell 

```
docker exec -it containername /bin/bash
```


