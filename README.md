# Microservice Example: Task queues with Celery and RabbitMQ

This project contains the source code and Kubernetes manifests for Django Celery application.

It contains the following Microservices
- Web app (mysite)
- Worker app (myworker)
- RabbitMQ

# How to run
Prerequisites: We need to have Kubernetes configured and accessed using `kubectl`
```sh
kubectl create secret generic rabbitmq-config --from-literal=erlang-cookie=this-is-good-enough
kubectl create -f rabbitmq.yaml
kubectl create -f mysite.yaml
kubectl create -f myworker.yaml
```
Confirm
```sh
kubectl get pods
NAME                      READY     STATUS    RESTARTS   AGE
mysite-75d7848dc4-8f7rc   1/1       Running   0          22h
myworker-9bb67c65-2jtdc   1/1       Running   0          22h
rabbitmq-0                1/1       Running   0          22h
rabbitmq-1                1/1       Running   0          1h
rabbitmq-2                1/1       Running   0          22h
```
`kubectl get service` will help you to get the external IP addresses of all services.

```
NAME                  TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                       AGE
kubernetes            ClusterIP   10.96.0.1        <none>        443/TCP                       5d
mysite                NodePort    10.97.86.194     <none>        8000:32448/TCP                5d
myworker              NodePort    10.108.146.157   <none>        8000:32248/TCP                22h
rabbitmq              ClusterIP   None             <none>        5672/TCP,4369/TCP,25672/TCP   22h
rabbitmq-management   NodePort    10.103.130.130   <none>        15672:30025/TCP               22h
```
In our case, You can access the web at http://localhost:32448 and rabbitmq management at http://localhost:30025