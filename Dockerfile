FROM node:16.13.1-alpine

RUN apk add -U subversion

FROM python:latest

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
