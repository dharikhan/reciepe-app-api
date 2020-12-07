FROM python:3.10-alpine
MAINTAINER dharitech ltd


ENV PYTHONUNBUFFERED 1

COPY ./requirement.txt/requirement.txt
RUN pip install -r /requirement.txt

RUN makrdir /app
WORKDIR /appCOPY ./app /app

RUN adduser -D user
USER user
