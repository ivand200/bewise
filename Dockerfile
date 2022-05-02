FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . /src/

RUN apt-get update

WORKDIR /src

RUN pip install -r requirements.txt