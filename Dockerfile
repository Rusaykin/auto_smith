FROM alpine

RUN apk add --no-cache curl wget busybox-extras netcat-openbsd python py-pip bash

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
