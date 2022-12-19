FROM python:3.11.1-alpine
ARG run_env=development
ENV env $run_env
WORKDIR /c/Projects/auto_smith-docker
VOLUME /test_results

RUN apk update && apk upgrade && apk add bash

COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
CMD pytest -s -v tests/* --alluredir=test_results