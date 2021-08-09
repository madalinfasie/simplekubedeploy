# Simple Kubernetes Deployment

Deploy a simple Flask api that requires a persistent volume

# Installation steps

1. Start minikube cluster: `minikube start`

2. Link minikube to the local docker repository to pull local images: `eval $(minikube docker-env)`

3. Build the docker image: `docker build -t api_flask .`

4. Deploy the API: `kubectl apply -f api_deployment.yaml`

5. Check the pods: `kubectl get pods`

6. Open the app in the browser: 
    - Get the cluster IP: `minikube ip`
    - Get cluster NodePort: `kubectl get deployments` or `kubectl describe deployment api-flask`

