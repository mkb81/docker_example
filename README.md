# Just a small Docker example

This is just to understanding [Docker](www.docker.com)  
and how to setup PyCharm IDE for the development.

## Using

### Create Docker image

Clone this repro on your local computer then 
you will find the Dockerfile inside the docker sub folder.

To build a new Docker image type the following command in path /docker_example

    docker build -t counter:latest -f docker/Dockerfile .
    
the build process can take some time.

If the build process is successful you can check your new Docker image

    docker images

and you should see a output like this
    
    REPOSITORY        TAG               IMAGE ID       CREATED          SIZE
    counter           latest            d21e4798517f   13 minutes ago   62.2MB


### Start Docker container

You can start the Docker image with this command

    docker run -it counter:latest

or with
    
    docker-compose up
