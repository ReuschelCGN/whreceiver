# Docker image for Raw WH Receiver 2

FROM python:3.8.10-slim

RUN export DEBIAN_FRONTEND=noninteractive && apt-get update \
&& apt-get install -y --no-install-recommends
RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt
ENV PYTHONUNBUFFERED 1
COPY . /usr/src/app/

CMD ["python3", "whreceiver2_raw.py"]
