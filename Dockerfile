FROM alpine:3.16

COPY requirements.txt .

RUN python -m pip install

RUN pip install -r requirements.txt

COPY . .
