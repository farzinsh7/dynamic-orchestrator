FROM python:3.11.7-slim-bullseye

LABEL maintainer="farzinnater@gmail.com"

ENV PYTTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY ./requirements.txt .

RUN apt update
RUN apt install memcached -y
RUN apt install nano -y
RUN apt install procps -y
RUN apt install telnet -y
RUN apt install net-tools -y
RUN touch gunicorn.log
RUN chmod 666 gunicorn.log
RUN mkdir tmp
RUN chmod 777 tmp
# RUN export PROMETHEUS_MULTIPROC_DIR=./tmp

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./core .
COPY ./envs .