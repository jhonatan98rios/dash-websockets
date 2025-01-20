# Websocket Dash App

# Enable minikube
```bash
minikube start
minikube addons enable registry minikube docker-env
minikube -p minikube docker-env --shell powershell | Invoke-Expression
```

# Server

## Create a image
```bash
    docker build -t websockets-echo-fastapi-server -f Dockerfile.server .
```

## Run the container (optional)
```bash
    docker run -it --rm -d -p 3000:3000 --name websockets-echo-fastapi-server websockets-echo-fastapi-server
```

## Tag image too use on minukube registry
```bash
    docker tag websockets-echo-fastapi-server 127.0.0.1:5000/websockets-echo-fastapi-server
```

## Push to minukube registry
```bash
    docker push 127.0.0.1:5000/websockets-echo-fastapi-server
```

---

# Client

## Create a image
```bash
    docker build -t websockets-echo-fastapi-client -f Dockerfile.client .
```

## Run the container (optional)
```bash
    docker run -it --rm -d -p 8050:8050 --name websockets-echo-fastapi-client websockets-echo-fastapi-client
```

## Tag image too use on minukube registry
```bash
    docker tag websockets-echo-fastapi-client 127.0.0.1:5000/websockets-echo-fastapi-client
```

## Push to minukube registry
```bash
    docker push 127.0.0.1:5000/websockets-echo-fastapi-client
```

---

# Helm and K8S

## Install Chart on Kubernetes
```bash
    helm install websockets-chat-helm ./websockets-chat-helm
```

## Port Forward
```bash
    minikube service websockets-chat-helm-backend
```