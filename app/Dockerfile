FROM python:3.6
MAINTAINER thanhnb "bathanhtlu@gmail.com"

RUN apt-get update && apt-get -y install build-essential \
libssl-dev libffi-dev python-dev \
libsasl2-dev python-dev libldap2-dev \
libssl-dev

RUN apt-get install -y postgresql postgresql-contrib libpq-dev

RUN apt install netcat -y

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app/

COPY ./create_user.sh /usr/src/app/create_user.sh

RUN chmod +x /usr/src/app/create_user.sh

ENTRYPOINT ["bash", "-x", "/usr/src/app/create_user.sh"]
