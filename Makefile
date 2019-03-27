download-swagger-ui:
	wget --no-clobber https://files.pythonhosted.org/packages/0e/bb/d00f72e512784af20e368d2ecd5868c51a5aa3688d26ace5f4391651a3ce/swagger_ui_bundle-0.0.3-py3-none-any.whl

install:
	make download-swagger-ui
	python -m pip install swagger_ui_bundle-0.0.3-py3-none-any.whl
	python -m pip install -r requirements.txt
	python -m pip install -e .

run:
	cd server && python -m openapi_server

generate:
	wget http://central.maven.org/maven2/org/openapitools/openapi-generator-cli/3.2.3/openapi-generator-cli-3.2.3.jar \
		--no-clobber \
		-O openapi-generator-cli.jar || echo 'Skipped downloading'
	java -jar openapi-generator-cli.jar generate -i api/ReasonerApi0.9.yaml -g python-flask -o server
	java -jar openapi-generator-cli.jar generate -i api/beacon-aggregator-api.yaml -g python -o client
	# Replace the generated __main__ file with our custom __main__ file
	rm server/openapi_server/__main__.py
	cp __main__.py-template server/openapi_server/
	mv server/openapi_server/__main__.py-template server/openapi_server/__main__.py

build:
	make download-swagger-ui
	docker build -t ncats:kba-reasoner .

start:
	docker run -d --rm -p 8080:8080 --name kbaR ncats:kba-reasoner

ssh:
	docker exec -it kbaR /bin/bash

stop:
	docker stop kbaR

log:
	docker logs kbaR
