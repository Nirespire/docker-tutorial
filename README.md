# docker-tutorial

## Prerequisites

- Install [docker](https://www.docker.com/get-started)
- Install [docker-compose](https://docs.docker.com/compose/install/)

## Getting Started

Note: Make sure to stop running containers between steps, else you might encounder errors.

If a container is running in the background using the `-d` flag, you can stop it with:

`docker ps` to find the running containers and

`docker stop <CONTAINER ID>` to stop a running container

### Run a MongoDB in a Docker container

`docker run --name my-mongo –d –p 27017:27017 mongo`

### Run this Python app by itself

`pip install -r requirements.txt`

`python app.py`

Navigate to http://localhost:8080

### Run this Python app in a Docker container

`docker build -t mypythonapp .`

`docker run -p 8080:8080 --name mypythoncontainer mypythonapp`

### Run this Python app with Redis in containers using Docker Compose

`docker-compose up`

### Run Graylog with multiple components using Docker Compose

`cd graylog_example`
`docker-compose up`