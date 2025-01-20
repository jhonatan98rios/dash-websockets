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

## Create or Update a image
```bash
    docker build -t websockets-dash-client -f Dockerfile.client .
```

## Run the container (optional)
```bash
    docker run -it --rm -d -p 8050:8050 --name websockets-dash-client websockets-dash-client
```

## Tag image too use on minukube registry
```bash
    docker tag websockets-dash-client 127.0.0.1:5000/websockets-dash-client
```

## Push to minukube registry
```bash
    docker push 127.0.0.1:5000/websockets-dash-client
```

---

# Helm and K8S

## Install Chart on Kubernetes
```bash
    helm install websockets-echo-fastapi-helm ./websockets-echo-fastapi-helm
```

## Port Forward
```bash
    minikube service websockets-echo-fastapi-helm-client
    minikube service websockets-echo-fastapi-helm-server
```

# Updating the chart
```bash
    helm upgrade websockets-echo-fastapi-helm ./websockets-echo-fastapi-helm
```

## Uninstall Chart
```bash
    helm delete websockets-echo-fastapi-helm
```

