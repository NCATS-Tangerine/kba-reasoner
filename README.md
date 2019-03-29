# KBA Reasoner

This application wraps the [Knowledge Beacon Aggregator](https://github.com/NCATS-Tangerine/beacon-aggregator) 
with the [NCATS Reasoner Application programming Interface](https://github.com/NCATS-Tangerine/NCATS-ReasonerStdAPI).

Install and run without docker:

```
# Python 3.6 or better can be used
virtualenv -p python3.7 venv
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
