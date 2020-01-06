openapi-generator:
	echo "(Re-)installing OpenAPI Generator Tool"
	curl https://raw.githubusercontent.com/OpenAPITools/openapi-generator/master/bin/utils/openapi-generator-cli.sh > /usr/local/bin/openapi-generator-cli
	chmod u+x /usr/local/bin/openapi-generator-cli
	openapi-generator-cli version

download-swagger-ui:
	wget --no-clobber https://files.pythonhosted.org/packages/0e/bb/d00f72e512784af20e368d2ecd5868c51a5aa3688d26ace5f4391651a3ce/swagger_ui_bundle-0.0.3-py3-none-any.whl

install:
	make download-swagger-ui
	python -m pip install swagger_ui_bundle-0.0.3-py3-none-any.whl
	python -m pip install -r requirements.txt
	python -m pip install -e .

run:
	cd server && python -m reasoner_server

validate:
	./generate.sh validate

generate:
	./generate.sh server
	./generate.sh client
	# Replace the generated __main__ file with our custom __main__ file
	rm server/reasoner_server/__main__.py
	cp __main__.py-template server/reasoner_server/__main__.py

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
