FROM python:3.7

COPY . /root

WORKDIR /root

RUN pip install -r requirements.txt


