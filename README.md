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
To be continued

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
docker run --rm -it -p 5000:5000 cmsc-495-project
```

TBD
