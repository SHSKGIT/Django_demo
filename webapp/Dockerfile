FROM python:3.9

MAINTAINER JW

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /ListingLlama/webapp

WORKDIR /ListingLlama/webapp

ADD . /ListingLlama/webapp

RUN pip3.9 install -r requirements.txt

RUN chmod +x ./start.sh