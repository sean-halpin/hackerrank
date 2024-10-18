# Kubernetes Core Concepts

## What is Kubernetes?
- Kubernetes is an open-source platform designed to automate deploying, scaling, and operating application containers.
- Kubernetes is a portable, extensible, open-source platform for managing containerized workloads and services, that facilitates both declarative configuration and automation.

## Why Kubernetes?
- **Orchestration**: Kubernetes allows you to define how your applications should run and scale.
- **High Availability**: Kubernetes ensures that your applications are highly available by running multiple instances of the application.
- **Scalability**: Kubernetes allows you to scale your applications up and down.
- **Load Balancing**: Kubernetes can distribute network traffic to multiple instances of an application.
- **Self-Healing**: Kubernetes can detect and restart failed instances of your application.
- **Automated Rollouts & Rollbacks**: Kubernetes can roll out new versions of your application without downtime.
- **Storage Orchestration**: Kubernetes can automatically mount storage systems of your choice, such as local storage, public cloud providers, and more.
- **Secrets & Configuration Management**: Kubernetes can manage sensitive information and configuration details for your applications.

## Kubernetes Architecture
- **Master Node**: The master node is responsible for managing the Kubernetes cluster. It is responsible for maintaining the desired state of the cluster.
- **Worker Node**: The worker nodes are the machines where your applications run. The worker nodes communicate with the master node to receive instructions and report back their status.

## Kubernetes Components
- **API Server**: The API server is the entry point for all the REST commands used to control the cluster.
- **etcd**: etcd is a consistent and highly-available key-value store used as Kubernetes' backing store for all cluster data.
- **Scheduler**: The scheduler is responsible for distributing work or containers across multiple nodes.
- **Controller Manager**: The controller manager is responsible for regulating the state of the cluster, such as detecting and responding to node failures.
- **Kubelet**: The kubelet is the primary "node agent" that runs on each node. It ensures that containers are running in a pod.
- **Kube Proxy**: The kube-proxy is a network proxy that runs on each node in your cluster, implementing part of the Kubernetes Service concept.
- **Container Runtime**: The container runtime is the software that is responsible for running containers.

## Kubernetes Objects
- **Pod**: A pod is the smallest deployable unit in Kubernetes. A pod encapsulates one or more containers, storage resources, a unique network IP, and options that govern how the container(s) should run.
- **Service**: A service is an abstraction that defines a logical set of pods and a policy by which to access them.
- **Volume**: A volume is a directory that is accessible to all containers in a pod.
- **Namespace**: A namespace is a way to divide cluster resources between multiple users.
- **Deployment**: A deployment is a way to declaratively manage a pod or pods. The deployment maintains a set of identical pods, ensuring that they have the correct configuration and that the right number of them is running.
- **ReplicaSet**: A replica set is a way to run multiple instances of a pod.
- **StatefulSet**: A stateful set is a way to run multiple instances of a pod with unique identities.
- **DaemonSet**: A daemon set ensures that all (or some) nodes run a copy of a pod.

## Kubernetes Commands
- **kubectl get pods**: List all pods in the current namespace.
- **kubectl get services**: List all services in the current namespace.
- **kubectl get deployments**: List all deployments in the current namespace.
- **kubectl get nodes**: List all nodes in the current cluster.
- **kubectl create -f pod-definition.yml**: Create a pod using the definition file.
  - Example pod definition file:
    ```yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: myapp-pod
      labels:
        app: myapp
    spec:
      containers:
        - name: nginx-container
          image: nginx
    ```
- **kubectl create -f service-definition.yml**: Create a service using the definition file.
  - Example service definition file:
    ```yaml
    apiVersion: v1
    kind: Service
    metadata:
      name: myapp-service
    spec:
      selector:
        app: myapp
      ports:
        - protocol: TCP
          port: 80
          targetPort: 80
    ```
- **kubectl create -f deployment-definition.yml**: Create a deployment using the definition file.
  - Example deployment definition file:
    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: myapp-deployment
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: myapp
      template:
        metadata:
          labels:
            app: myapp
        spec:
          containers:
            - name: nginx-container
              image: nginx
    ```
- **kubectl describe pod myapp-pod**: Describe a pod.
- **kubectl describe service myapp-service**: Describe a service.
- **kubectl describe deployment myapp-deployment**: Describe a deployment.
- **kubectl delete pod myapp-pod**: Delete a pod.
- **kubectl delete service myapp-service**: Delete a service.
- **kubectl delete deployment myapp-deployment**: Delete a deployment.
- **kubectl apply -f pod-definition.yml**: Apply changes to a pod using the definition file.
- **kubectl apply -f service-definition.yml**: Apply changes to a service using the definition file.
- **kubectl apply -f deployment-definition.yml**: Apply changes to a deployment using the definition file.
- **kubectl scale deployment myapp-deployment --replicas=4**: Scale a deployment to 4 replicas.
- **kubectl expose deployment myapp-deployment --type=NodePort --port=8080**: Expose a deployment as a NodePort service on port 8080.
- **kubectl get pods -o wide**: List all pods in the current namespace with additional details.
- **kubectl get pods -o wide --show-labels**: List all pods in the current namespace with additional details and labels.
- **kubectl get pods -o wide --sort-by=.status.phase**: List all pods in the current namespace sorted by the phase.
- **kubectl get pods -o wide --sort-by=.metadata.creationTimestamp**: List all pods in the current namespace sorted by the creation timestamp.
- **kubectl get pods -o wide --sort-by=.spec.nodeName**: List all pods in the current namespace sorted by the node name.
- **kubectl get pods -o wide --sort-by=.metadata.name**: List all pods in the current namespace sorted by the name.
- **kubectl get pods -o wide --sort-by=.status.podIP**: List all pods in the current namespace sorted by the pod IP.
- **kubectl get pods -o wide --sort-by=.status.startTime**: List all pods in the current namespace sorted by the start time.
- **kubectl get pods -o wide --sort-by=.status.hostIP**: List all pods in the current namespace sorted by the host IP.

## Kubernetes Resources
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Kubernetes API Reference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.22/)
- [Kubernetes Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
- [Kubernetes Interactive Tutorial](https://kubernetes.io/docs/tutorials/kubernetes-basics/)

## Kubernetes Tools
- **kubectl**: The Kubernetes command-line tool.
- **minikube**: A tool that makes it easy to run Kubernetes locally.
- **kubeadm**: A tool to create, upgrade, and maintain a Kubernetes cluster.
- **kops**: A tool to create, upgrade, and maintain production-grade, highly available Kubernetes clusters.
- **kubectx**: A tool to switch between clusters and namespaces.
- **kubens**: A tool to switch between Kubernetes namespaces.
- **k9s**: A terminal-based UI to interact with your Kubernetes clusters.
- **Lens**: A Kubernetes IDE that provides a full view of your clusters.
- **Octant**: A tool to interact with your Kubernetes clusters.
- **KubeForwarder**: A Kubernetes port-forwarding tool.
- **Kube-ops-view**: A read-only system dashboard for multiple K8s clusters.
- **Kubeval**: A tool to validate your Kubernetes configuration files.