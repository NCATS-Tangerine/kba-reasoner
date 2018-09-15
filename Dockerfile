FROM python:3

RUN mkdir -p /usr/src

COPY /server /usr/src/server
COPY /client /usr/src/client
COPY requirements.txt /usr/src/requirements.txt
COPY config.yaml /config.yaml

# include --no-cache-dir flag when development finalizes?
RUN pip install --upgrade pip && \
    pip install -r /usr/src/requirements.txt && \
    pip install /usr/src/server/ && \
    pip install /usr/src/client/ 

WORKDIR /usr/src/server

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "reasoner_server"]
