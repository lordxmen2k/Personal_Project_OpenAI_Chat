# Docker Container Deployment Guide

This guide walks you through building a Docker image from a Dockerfile and running the container on port 5050.

## Prerequisites

Before you begin, make sure you have the following installed:
- Docker

## Building the Docker Image

To build the Docker image from your Dockerfile, run the following command in the directory where your Dockerfile is located:

```bash
docker build -t your-image-name .
```

Replace `your-image-name` with the name you want to give your Docker image.

## Running the Docker Container

Once the image is built, you can run a container from that image and map the internal port `5000` to the external port `5050` using:

```bash
docker run -p 0.0.0.0:5000:5000 -e OPENAI_SECRET_KEY='YOUR-API-KEY-HERE' openai-chat
```

Make sure that the application inside the container is configured to listen on port `5000`, as indicated in the Dockerfile by the `EXPOSE 5000` directive.

Access your application by visiting `http://localhost:5051` on your web browser.

## Stopping the Docker Container

To stop the running container:

1. List the running containers:

   ```bash
   docker ps
   ```

2. Stop the container using the container ID or name:

   ```bash
   docker stop <container-id-or-name>
   ```

That's it! You have successfully built and run a Docker container using port 5050.
