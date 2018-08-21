# KBA Reasoner

NCATS Translator Reasoner API wrapper for the Knowledge Beacon Aggregator.

## Running the Application

Two options:

1. Run the application within Docker (preferred)
2. Run the application directly

### 1. Running under Docker

#### Installation of Docker

If you choose to run the dockerized versions of the applications, you'll obviously need to [install Docker first](https://docs.docker.com/engine/installation/) in your target Linux operating environment (bare metal server or virtual machine running Linux).

For our installations, we typically use Ubuntu Linux, for which there is an [Ubuntu-specific docker installation using the repository](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/#install-using-the-repository).

Note that you should have 'curl' installed first before installing Docker:

```
$ sudo apt-get install curl
```

For other installations, please find instructions specific to your choice of Linux variant, on the Docker site.

#### Testing Docker

In order to ensure that docker is working correctly, run the following command:

```
$ sudo docker run hello-world
```

This should result in the following output:
```
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
ca4f61b1923c: Pull complete
Digest: sha256:be0cd392e45be79ffeffa6b05338b98ebb16c87b255f48e297ec7f98e123905c
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://cloud.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/engine/userguide/
```
#### Configuring the Application

Copy the *config.yaml-template* into *config.yaml*.

You can customize the *config.yaml* to set the desired TCP port for the application. Alternately, you can use the  **-p** directive in your docker *run* command (see below) to dynamically remap your Rhea application to publish the default port 8080 on another port of interest, e.g. **-p 8090:8080** 

To build the Docker container, run the following command

```
 $ cd ..  # make sure you are back in the root project directory
 $ sudo docker build -t ncats:kba-reasoner .
```

The **-t** directive explicitly names the Docker image for your container.  This command make take some time to execute, as it is downloading and building your docker container.

To run the system, run the following command:

```
$ sudo docker run -d --rm -p 8090:8080 --name kbaR ncats:kba-reasoner
```

The **-n** explicitly names the Docker container (e.g. to 'kbaR'); **-d** parameter runs the application as a daemon; and the **-rm** directive forces deletion of the Docker container when it is stopped. To troubleshoot the Docker, you may sometimes wish to omit the latter two directives.

To view the Docker (running) logs for the beacon, run the following:

```
$ sudo docker logs -f kbaR
```

To shut down the system, run the following:

```
$ sudo docker stop kbaR
```

### 2. Directly (code snippets are for Linux)

#### Getting started

Create a fresh virtual environment
```
virtualenv -p python3.7 venv
source venv/bin/activate
```

Install the project requirements:
```
pip install -r requirements.txt
```

Setup the config file by copying the template file:
```
cp config.yaml-template config.yaml
``` 
(Optionally) change the port setting in `config.yaml` to match the port upon which you wish to publish the rhea beacon (if not port 8080).

Navigate into the `/server` directory and run:
```
python setup.py install
```

Then navigate into the `/client` directories and do the same.

Then navigate into the `/server` directory and run the program with:
```
python -m swagger_server
```

The Swagger UI can be found at `{basepath}/ui/`, e.g. `localhost:8080/ui/`

#### Configuring the Wrapper

You can change the port in the `config.yaml` file.
