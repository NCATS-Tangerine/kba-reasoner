#!/bin/sh
# This script downloads openapi-generator-cli.jar from https://github.com/OpenAPITools/openapi-generator
# into a hidden directory and then uses it to generate server and client Python project stubs

#############################
###       Constants       ###
#############################

# This is a whitespace (space or tab) delimited list of lines that will be added to .openapi-generator-ignore prior to code generation, if they are not already present.
IGNORE_LIST=""

# This is where we will download openapi-generator-cli.jar from latest release 4.*.* version
OPENAPI_GENERATOR_JAR_LOCATION="http://central.maven.org/maven2/org/openapitools/openapi-generator/4.2.2/openapi-generator-cli-4.2.2.jar -O .openapi-generator/openapi-generator-cli.jar"

# Here we define the names of the directories that the server and client projects will be generated into
PROJECT_NAME="kba-reasoner"

SERVER_OUTPUT_DIR="server"
SERVER_PACKAGE_NAME="reasoner_server"
SERVER_PACKAGE_VERSION="0.9.2"

CLIENT_OUTPUT_DIR="client"
CLIENT_PACKAGE_NAME="kba_client"
CLIENT_PACKAGE_VERSION="1.1.1"

#############################
###        Methods        ###
#############################

# Called when there is an error with how the script is being used
usage() {
echo "usage: $(basename "$0") <command> <specification> -- uses OpenAPI Generator to generate a python project stub

	command:
		server		to generate a server
		client		to generate a client
		clean		to delete .openapi-generator/openapi-generator-cli.jar

	specification:
		path to a json or yaml specification file to be used for generating the server or client project stub"
	exit 1
}

# Ensures that the .openapi-generator-ignore file is set up and in place
ensureValidIgnoreFile() {
	DIRECTORY="$1"
	IGNORE_FILE="$DIRECTORY/.openapi-generator-ignore"

	if [ ! -f "$IGNORE_FILE" ]; then
		# Swagger automatically creates an empty .openapi-generator-ignore file, so this must mean that the project hasn't ever been generated before.
		# The ignore functionality applies not just to overwriting preexisting files, but also creating files. So we don't want an ignore file active in this case.
		return
	fi

	for FILE_NAME in $IGNORE_LIST; do
		ANY_DIR_FILE_NAME='**/'"$FILE_NAME"

		if ! grep -q -x "$ANY_DIR_FILE_NAME" "$IGNORE_FILE" ; then
			echo "$ANY_DIR_FILE_NAME" >> "$IGNORE_FILE"
		fi

		if ! grep -q -x "$FILE_NAME" "$IGNORE_FILE" ; then
			echo "$FILE_NAME" >> "$IGNORE_FILE"
		fi
	done

}

#############################
###     Script Logic      ###
#############################

# Get the command
if [ -z "$1" ]; then
	usage
else
	COMMAND="$1"

	if   [ "$COMMAND" = client ]; then
		:
	elif [ "$COMMAND" = server ]; then
		:
	elif [ "$COMMAND" = clean ]; then
		# redirect output to /dev/null to prevent it from printing
		rm .openapi-generator/openapi-generator-cli.jar 2> /dev/null || echo "There is nothing to clean"
		exit 0
	else
		echo "Invalid command\n"
		usage
	fi
fi

# Get the specification file
if [ -z "$2" ]; then
		if [ "$COMMAND" = client ]; then
			SPECIFICATION_FILE_PATH=kba_api/beacon-aggregator-api.yaml
	    elif [ "$COMMAND" = server ]; then
			SPECIFICATION_FILE_PATH=reasoner_api/API/TranslatorReasonersAPI.yaml
		else
			echo "No default for unknown specification file\n"
			usage
		fi
else
	SPECIFICATION_FILE_PATH="$2"

	if [ "${SPECIFICATION_FILE_PATH#*.yaml}" != $SPECIFICATION_FILE_PATH ]; then
		:
	elif [ "${SPECIFICATION_FILE_PATH#*.json}" != $SPECIFICATION_FILE_PATH ]; then
		:
	else
		echo "Invalid specification file\n"
		usage
	fi
fi

# Attempt to download openapi-generator-cli.jar if it doesn't already exist
if [ -f ".openapi-generator/openapi-generator-cli.jar" ]; then
	:
else
	mkdir -p .openapi-generator

	# wget creates a file whether or not it's able to download it, so if there's a download error we want to delete the file that was created.
	wget $OPENAPI_GENERATOR_JAR_LOCATION || rm -f .openapi-generator/openapi-generator-cli.jar

	# If download failed then exit
	if [ ! -f .openapi-generator/openapi-generator-cli.jar ]; then
		echo "Failed to download openapi-generator-cli.jar"
		exit 1
	fi
fi

# Use openapi-generator-cli.jar to generate the server and client stub
if [ "$COMMAND" = validate ]; then

	java -jar .openapi-generator/openapi-generator-cli.jar generate -i $SPECIFICATION_FILE_PATH -g python -o $CLIENT_OUTPUT_DIR \
	          -D packageName=$CLIENT_PACKAGE_NAME -D projectName=$PROJECT_NAME -D packageVersion=$SERVER_PACKAGE_VERSION

	exit 0

elif [ "$COMMAND" = client ]; then
	ensureValidIgnoreFile "$CLIENT_OUTPUT_DIR"

openapi-generator generate  --input-spec=kba_api/beacon-aggregator-api.yaml \
                    --model-package=model \
                    --output=client \
                    --generator-name=python \
                    --additional-properties="\
--packageName=client.kba_client,\
--projectName=kba-reasoner,\
—-packageVersion=\"1.1.1\",\
--packageUrl=https://github.com/NCATS-Tangerine/kba-reasoner/tree/master/client"

	java -jar .openapi-generator/openapi-generator-cli.jar generate -i $SPECIFICATION_FILE_PATH -g python -o $CLIENT_OUTPUT_DIR \
	          -D packageName=$CLIENT_PACKAGE_NAME -D projectName=$PROJECT_NAME -D packageVersion=$SERVER_PACKAGE_VERSION

	exit 0

elif [ "$COMMAND" = server ]; then
	ensureValidIgnoreFile "$SERVER_OUTPUT_DIR"

	openapi-generator generate --input-spec=reasoner_api/API/TranslatorReasonersAPI.yaml \
                    --model-package=model \
                    --output=server \
                    --generator-name=python-flask \
                    --additional-properties="\
--packageName=server.reasoner_server,\
--projectName=kba-reasoner,\
—-packageVersion=\"0.9.2\",\
--packageUrl=https://github.com/NCATS-Tangerine/kba-reasoner/tree/master/server,\
--serverPort=8080"

	java -jar .openapi-generator/openapi-generator-cli.jar generate -i $SPECIFICATION_FILE_PATH -g python-flask \
	          -o $SERVER_OUTPUT_DIR  -D packageName=$SERVER_PACKAGE_NAME -D projectName=$PROJECT_NAME
	          -D packageVersion=$CLIENT_PACKAGE_VERSION
	exit 0

else
	echo "Something went wrong, script should have terminated already"
	exit 1
fi


