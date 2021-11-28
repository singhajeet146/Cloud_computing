# Sentiment Classification

This project is created to show the capability of docker and kubernetes on GCP.
Especially this projects focuses on auto scale and rolling update strategy concept.


In order to run this project please folow below steps.
1. Download ans install the Google Cloud SDK.
2. Create Cluster on GKE.
3. Install and Run the Docker.
4. Build & Push an Image To Google Cloud by running docker_push.sh file

> command
```
sh docker_push.sh

```

5. Run deployment.yml files

> command
```
kubectl apply -f deployment.yml
```

or run below command

```
kubectl create deployment ccproj --image=gcr.io/<proj-id>/cad-site:<version>

```

6. Exposing the Deployment

> command
```
kubectl expose deployment ccproj --type LoadBalancer --port 80 --target-port 5021
```

7. Run below command and copy EXTERNAL-IP
> command
```
kubectl get service
```

8. run curl command
> command
```
curl EXTERNAL-IP/end-point
```
