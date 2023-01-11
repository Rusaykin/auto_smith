#FROM python:3.11.1-alpine
FROM python
ARG run_env=development
ENV env $run_env
WORKDIR /test_project/
VOLUME /test_results

#RUN apk update && apk upgrade && apk add bash

COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
CMD python -m pytest -s --alluredir=test_results/ /test_project/tests/
#CMD pytest -s -v /test_project/tests/* --alluredir=/test_results

#FROM python
#WORKDIR /test_project/
#COPY requirements.txt .
#RUN pip install -r requirements.txt
#ENV ENV=dev
#CMD python -m pytest -s --alluredir=test_results/ /test_project/tests/