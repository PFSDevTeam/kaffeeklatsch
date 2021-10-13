# cmsc-495-project
CMSC 495 Final Project

This is the repository for the final project for CMSC 495. The setup / shell has not yet been completed. look here for running instructions in the next few days. 

## Technology Stack

- Python: Flask
- Docker

## Installation Instructions

### Docker

To install docker visit: https://www.docker.com/get-started

**Docker is a containerization tool that is NOT required for local development. Standard Python run commands will work. Instructions for both methods of running the application will be included in the 'Running Instructions' setting

#### Docker Compose (live reload) (recommended)

to build and run the project using docker-compose (recommended)

use the following command in the project root directory after docker is installed:
```
docker-compose up
```

to stop the application run the following command:
```
docker-compose  down
```

to force the application to rebuild the images with a new run you can use:
```
docker-compose up --build
```

#### Build

to build the project container run the following from the root directory 

using the build script on linux:
```
./docker-build.sh
```

**OR**

Using the docker build command:

```
docker build -t cmsc-495-project .
```

### local installation

To install the project on your local machine, first install python3 and pip are installed and current

next use pip to install the the dependancies

```
pip install -r requirements.txt
```

## Running instructions

### Local Python

To run on your local machine using your active python installation you can use

Note: you will have had to install the dependancies first

```
flask run
```

### Docker

To run in docker use the following command after the container has been built (see build section)

Using the run script on linux:
```
./docker-run.sh
```

**OR**

Using the docker run command:
```
docker run --rm -it -p 5000:5000 --name kaffeeklatsch cmsc-495-project

```

## Stopping Instructions

### Docker

To stop the docker container and prune images you can:

use the stop script:

```
./docker-stop.sh
```

**OR**

use the docker stop command:
```
docker stop (CONTAINER NAME OR ID)

# e.g

docker stop kaffeeklatsch

# OR

docker stop 6c9d74d7e2ce
```