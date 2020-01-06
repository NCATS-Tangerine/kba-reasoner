# KBA Reasoner

This application wraps the [Knowledge Beacon Aggregator](https://github.com/NCATS-Tangerine/beacon-aggregator) 
with the [NCATS Reasoner Application programming Interface](https://github.com/NCATS-Tangerine/NCATS-ReasonerStdAPI).

## Getting and Configuring the Project

The system may be run as a standalone application or within a Docker container. In this section, we assume direct 
execution as a standalone system (see below for Docker)

The **kba-reasoner** package is not yet available through PyPI, thus, to install, clone this repo using git.

```bash
git clone --recursive https://github.com/NCATS-Tangerine/kba-reasoner.git

# ... then  enter  into your cloned project repository
cd kba-reasoner
```

The code is now validated to work only with Python 3.7 only.  We recommend using a **virtualenv** to enforce this.

```bash
# Python 3.7 or better can be used

virtualenv -p python3.7 venv
source venv/bin/activate
```

## Running the System

There are two ways to run the system: directly as a standalone system or within a Docker container.

To install and run the code directly: 

```bash
make install
make run
```

To build and start the system within a Docker container:

```bash
make build
make start
```

You can also use `make log` to see the docker containers logs, and `make stop` to stop the docker container.

## Updating the Reasoner API Specification

The Makefile may also be used to regenerate the code.

First, the [OpenAPI Code Generator](https://openapi-generator.tech/docs/installation) needs to be installed. The
`Makefile` wraps the installation of the `bash` scripted version of the tool which may not work under all platforms but 
you can also manually install the tool and make it visible as a runnable binary or macro called `openapi-generator`. 
Note the use of `sudo` to run the `openapi-generator` target (since it installs the tool under `/usr/local/bin`) 

```bash
sudo make openapi-generator
```

There is a `validate` target to check the OpenAPI specifications, prior to regenerating the code:

```bash
make validate
```

The *validate* target calls a local shell script `generate.sh` in the root directory of the project.  This script 
checks for the presence of the [OpenAPI Code Generator](https://openapi-generator.tech/docs/installation) 
binary and attempts to install it if it is not yet installed on the computer. This installation may be problematic on  
some platforms (e.g. Microsoft Windows) but you can also manually install the tool. If you do this, you may need to 
override the OPENAPI_GENERATOR_CLI and OPENAPI_GENERATOR_CLI_PATH environment variables used by the generator script.
Even on Unix-type systems, the `generate.sh` script installation of the OpenAPI Code generator may fail if not run as 
'sudo' since the binary is being installed under _/usr/local/bin_, thus so you may need to run the above *validate* 
make target as sudo the first time, to ensure a sucessful installation (however, the installation processes does 
fix the execute permissions for general access, so 'sudo' shouldn't be needed afterwards).
 
After installing the `openapi-generator` tool and validating the API's, the code may be (re-)generated:

```bash
make code-generation
```

### The Gory Details...

Ideally, the aforementioned `make` process should work but, just in case, we provide more details on the whole code 
generation procedure here below.

#### The OpenAPI specifications

The KBA Reasoner is an implementation of the 

Refer to the [Python Flask server](./server) implementation of the Reasoner API wrapper of the KBA with 
a corresponding [Python client](./client).  

#### (Re-)Generating the Server and Client

The *client* is a direct Python web service client and the *server* is a simple Python Flask server implementation.

The implementation of the KBA Reasoner server system uses code generation from an 
[OpenAPI 3.* NCATS Reasoner API specification](./reasoner_api/API/TranslatorReasonersAPI.yaml), 
which is used as a template to generate the code base, which is then wired up by delegation to additional handler code.  
 
The implementation of the KBA client system uses code generation from an 
[OpenAPI 3.* KBA API specification](./kba_api/beacon-aggregator-api.yaml), 
which is used as a template to generate the code base, which is then wired up by delegation to additional handler code.  
 
The generated and other client/server code is found in the *client* and  *server* subfolders.

By [installing a local copy of the OpenAPI Code Generator](https://openapi-generator.tech/docs/installation), 
modified OpenAPI 3.0 YAML specifications can be processed to recreate the Python client and Python Flask server stubs.
Note that depending on how you install the OpenAPI Code Generator, the manner in which you execute the 
 `openapi-generator` command below will change accordingly (Note that the code generation processes are a bit more 
 streamlined and robust under Linux and OSX than Microsoft Windows).

The code generation commands are generally run from the root project directory directory.  First, one should check 
your new or modified OpenAPI YAML specifications using the _validate_ command:

```bash
openapi-generator validate (-i | --input-spec=)reasoner_api/API/TranslatorReasonersAPI.yaml
openapi-generator validate (-i | --input-spec=)kba_api/beacon-aggregator-api.yaml
```

If the specifications pass muster, then to recreate the Python Flask *server* stubs, the following command may 
be typed from within the root directory:

```bash
openapi-generator generate --input-spec=reasoner_api/API/TranslatorReasonersAPI.yaml \
                    --model-package=model \
                    --output=server \
                    --generator-name=python-flask \
                    --additional-properties="\
--packageName=server.reasoner_server,\
--projectName=kba-reasoner,\
—-packageVersion=\"0.9.2\",\
--packageUrl=c\
tree/master/server,\
--serverPort=8080"
```

and to recreate the KBA *client* Python access stubs, something along the lines of the following command is typed:

```bash
openapi-generator generate  --input-spec=kba_api/beacon-aggregator-api.yaml \
                    --model-package=model \
                    --output=client \
                    --generator-name=python \
                    --additional-properties="\
--packageName=client.kba_client,\
--projectName=kba-reasoner,\
—-packageVersion=\"1.1.1\",\
--packageUrl=https://github.com/NCATS-Tangerine/kba-reasoner/tree/master/client"
```

The [OpenAPI 3.0 'generate' command usage](https://openapi-generator.tech/docs/usage#generate) may be consulted
for more specific details on available code generation options and for acceptable program flag abbreviations (here we
used the long form of the flags).

The above commands are also wrapped inside of a `generate.sh` shell script in the root project directory and 
may also be invoked using the provide Makefile targets.

#### Repairing the Generated Code

In both cases, after generating the code stubs, a developer likely needs to repair the regenerated code a bit.

First, the code stubs must be reconnected to the (delegated) business logic to the REST processing front end as 
required to get the system working again.  Developers can scrutinize recent working releases of the code to 
best understand how the code stubs need to be reconnected or how to add new business logic.

Also, the *server* and *client* subdirectory _README.md_ and _setup.py_ files are overwritten by the code generation. 
These should be restored from the \*-master.\* versions of these files in each directory.
 
Finally, check if the `server/openapi_server/__main__.py` file has the correct Identifiers server port (8080).

For good measure, after such extensive rebuilding of the libraries, the 'pip' environment dependencies should also 
be updated, as documented for the client and server, prior to re-testing and using the updated software.
