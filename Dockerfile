FROM python:3.7

RUN mkdir -p /usr/src

WORKDIR /usr/src

COPY reasoner reasoner
COPY server server
COPY client client
COPY requirements.txt requirements.txt
COPY setup.py setup.py

RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir .

WORKDIR /usr/src/server

EXPOSE 8080

ENTRYPOINT ["python"]

CMD ["-m", "reasoner_server"]
