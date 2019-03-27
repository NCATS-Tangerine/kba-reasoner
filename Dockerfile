FROM python:3

RUN mkdir -p /usr/src

COPY /server /usr/src/server
COPY /client /usr/src/client
COPY requirements.txt /usr/src/requirements.txt
COPY config.yaml /config.yaml
COPY swagger_ui_bundle-0.0.3-py3-none-any.whl swagger_ui_bundle-0.0.3-py3-none-any.whl

# include --no-cache-dir flag when development finalizes?
RUN pip install --upgrade pip && \
    pip install swagger_ui_bundle-0.0.3-py3-none-any.whl && \
    pip install -r /usr/src/requirements.txt && \
    pip install /usr/src/server/ && \
    pip install /usr/src/client/

WORKDIR /usr/src/server

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "openapi_server"]
