FROM alpine:3.16

COPY requirements.txt .

RUN apt-get -y install python3-pip

RUN pip install -r requirements.txt

COPY . .
