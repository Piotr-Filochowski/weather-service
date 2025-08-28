FROM python:3.9 AS base

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY src src
RUN mkdir -p /logs
CMD [ "python3", "-u", "src/main.py"]