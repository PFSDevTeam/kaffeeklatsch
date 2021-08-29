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

```
docker build -t cmsc-495-project .
```

To be continued

## Running instructions

### Docker

To run in docker use the following command after the container has been built (see build section)

```
docker run -p 5000:5000 cmsc-495-project
```

TBD
