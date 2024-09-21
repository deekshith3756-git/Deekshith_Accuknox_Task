# Kubernetes Frontend-Backend Deployment

## Prerequisites:
- Docker
- Minikube
- kubectl

## Steps to Deploy:

1. Start Minikube:
    ```bash
    minikube start
    ```

2. Build Docker Images:
    ```bash
    eval $(minikube docker-env)
    docker build -t backend:v1 ./backend
    docker build -t frontend:v1 ./frontend
    ```

3. Apply Kubernetes Deployment Files:
    ```bash
    kubectl apply -f Deployment/backend-deployment.yaml
    kubectl apply -f Deployment/frontend-deployment.yaml
    ```

4. Access Frontend Service:
    ```bash
    minikube service frontend-service --url
    ```

## Running Automated Tests:
1. Install `requests` library:
    ```bash
    pip install requests
    ```

2. Run the test script:
    ```bash
    python test_integration.py
    ```
