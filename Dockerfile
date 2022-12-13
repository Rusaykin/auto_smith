FROM alpine:3.16

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
