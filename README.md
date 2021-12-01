# Just a small Docker example

This is just to understanding [Docker](www.docker.com)  
and how to use [PyCharm IDE](https://www.jetbrains.com/pycharm/) for the development.

The Docker image based on
* Alpine 3.14 Linux
* Python 3.9.8

## Using

### Create Docker image

Clone this repo to your local computer. After that go to folder

    /<path to the repro>/docker_example

Build new Docker image type the following console command

    docker build -t counter:latest -f docker/Dockerfile .
    
the build process can take some time.

If the build process is successful then check your new Docker image

    docker images

and you should see a output like this
    
    REPOSITORY        TAG               IMAGE ID       CREATED          SIZE
    counter           latest            d21e4798517f   13 minutes ago   62.2MB


### Start Docker container

You can start the Docker image with this command

    docker run -it counter:latest

or with
    
    docker-compose up


## Known issues

At time there is no colored output if the image is start with **docker-compose up**