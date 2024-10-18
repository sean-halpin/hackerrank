# Dockerfile

- A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image.

## Dockerfile commands

- **FROM**: Set the base image for the build.
- **LABEL**: Add metadata to an image.
- **RUN**: Execute a command in a new layer on top of the current image and commit the results.
- **COPY**: Copy files or directories from a source to a destination.
- **ADD**: Copy files, directories, or remote file URLs from a source to a destination.
- **CMD**: Provide defaults for an executing container.
- **WORKDIR**: Set the working directory for any RUN, CMD, ENTRYPOINT, COPY, and ADD instructions that follow it in the Dockerfile.
- **ARG**: Define a variable that users can pass at build-time to the builder with the docker build command using the --build-arg <varname>=<value> flag.
- **ENTRYPOINT**: Configure a container that will run as an executable.
- **EXPOSE**: Inform Docker that the container listens on the specified network ports at runtime.
- **ENV**: Set environment variables.
- **VOLUME**: Create a mount point for externally mounted volumes or other containers.
- **USER**: Set the user name or UID to use when running the image.
- **HEALTHCHECK**: Tell Docker how to test a container to check that it is still working.
- **SHELL**: Set the default shell used for the shell form of commands in the Dockerfile.
- **ONBUILD**: Add a trigger instruction to the image that will be executed at a later time when the image is used as the base for another build.
- **STOPSIGNAL**: Sets the system call signal that will be sent to the container to exit.
- **SHELL**: Set the default shell used for the shell form of commands in the Dockerfile.
- **MAINTAINER**: Set the author field of the generated images.

# Docker commands

- **docker build -t myapp:latest .**: Build an image using the Dockerfile in the current directory.
- **docker run myapp:latest**: Run a container using the specified image.
- **docker ps**: List all running containers.
- **docker ps -a**: List all containers (running and stopped).
- **docker stop mycontainer**: Stop a running container.
- **docker rm mycontainer**: Remove a stopped container.
- **docker images**: List all images.
- **docker rmi myimage:latest**: Remove an image.
- **docker exec -it mycontainer sh**: Execute a command inside a running container.
- **docker logs mycontainer**: Fetch the logs of a container.
- **docker pull myimage:latest**: Pull an image from a registry.
- **docker push myimage:latest**: Push an image to a registry.

# Docker networking

- **Bridge network**: The default network that bridges the Docker container to the host network.
- **Host network**: The container uses the host network directly.
- **Overlay network**: A network that spans multiple Docker daemons, enabling secure communication between containers on different hosts.
- **Macvlan network**: A network that assigns a MAC address to a container, making it appear as a physical device on the network.
- **None network**: The container has no network access.
- **Network plugins**: Third-party plugins that enable Docker networking.
- **Docker network commands**:
  - **docker network ls**: List all networks.
  - **docker network inspect bridge**: Inspect a network.
  - **docker network create --driver bridge my-bridge-network**: Create a bridge network.
  - **docker network connect my-bridge-network mycontainer**: Connect a container to a network.
  - **docker network disconnect my-bridge-network mycontainer**: Disconnect a container from a network.

# Docker storage

- **Volumes**: A data volume is a specially designated directory within one or more containers that bypasses the Union File System.
- **Bind mounts**: A bind mount is a mapping of a host file or directory to a container file or directory.
- **tmpfs mounts**: A tmpfs mount is stored in the host system's memory only and is never written to the host system's filesystem.
- **Storage drivers**: The storage driver controls how images and containers are stored and managed on your Docker host.
- **Docker storage commands**:
  - **docker volume ls**: List all volumes.
  - **docker volume inspect my-volume**: Inspect a volume.
  - **docker volume create my-volume**: Create a volume.
  - **docker volume rm my-volume**: Remove a volume.
  - **docker run -v my-volume:/path/in/container myimage:latest**: Mount a volume to a container.
  - **docker run -v /host/path:/container/path myimage:latest**: Mount a bind mount to a container.
  - **docker run --tmpfs /path/in/container myimage:latest**: Mount a tmpfs mount to a container.

# Docker Compose

- **Docker Compose**: A tool for defining and running multi-container Docker applications.
- **docker-compose.yml**: A YAML file that defines how Docker containers should behave in production.
- **Docker Compose commands**:
  - **docker-compose up**: Create and start containers.
  - **docker-compose down**: Stop and remove containers.
  - **docker-compose ps**: List containers.
  - **docker-compose logs**: Fetch the logs of containers.
  - **docker-compose exec mycontainer sh**: Execute a command inside a running container.
  - **docker-compose build**: Build or rebuild services.
  - **docker-compose pull**: Pull service images.
  - **docker-compose push**: Push service images.
  - **docker-compose config**: Validate and view the compose file.
  - **docker-compose images**: List images used by services.

# Kubernetes core concepts

# Kubernetes deployment object

- A deployment object is a higher-level concept that manages replica sets and provides declarative updates to pods along with a lot of other useful features.

## Kubernetes deployment object commands

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
- **kubectl get deployments**: List all deployments in the current namespace.
- **kubectl describe deployment myapp-deployment**: Describe a deployment.
- **kubectl delete deployment myapp-deployment**: Delete a deployment.
- **kubectl rollout status deployment/myapp-deployment**: Check the status of a deployment rollout.
- **kubectl set image deployment/myapp-deployment nginx=nginx:1.9.1**: Update the image of a deployment.
- **kubectl rollout history deployment/myapp-deployment**: Check the rollout history of a deployment.
- **kubectl rollout undo deployment/myapp-deployment**: Rollback a deployment to the previous version.
- **kubectl rollout undo deployment/myapp-deployment --to-revision=2**: Rollback a deployment to a specific revision.
- **kubectl scale deployment myapp-deployment --replicas=4**: Scale a deployment to a specific number of replicas.
- **kubectl autoscale deployment myapp-deployment --min=3 --max=6 --cpu-percent=80**: Autoscale a deployment based on CPU utilization.

# Kubernetes service object
