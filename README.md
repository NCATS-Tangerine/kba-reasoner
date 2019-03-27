# KBA Reasoner

Install and run without docker:

```
virtualenv -p python3.6 venv
source venv/bin/activate
make install
make run
```

Build and start docker container:

```
make build
make start
```
You can also use `make log` to see the docker containers logs, and `make stop` to stop the docker container.

To regenerate the code:
```
make generate
```
