FROM python:3.9-slim-buster

RUN apt-get -y update && \
    apt-get -y install redis-server

WORKDIR /app

COPY requirements.txt requirements.txt

RUN mkdir -p /etc/wingnut

COPY wingnut.yaml /etc/wingnut/

RUN pip3 install -r requirements.txt

COPY . .

RUN chmod 755 startup.sh 

CMD ["./startup.sh"]

