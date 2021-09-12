# pull official base image
FROM python:3.9.4

# install ffmpeg
RUN apt-get -y update
RUN apt-get -y upgrade

# set work directory
WORKDIR /usr/src/app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./wsgi-entrypoint.sh .

# copy project
COPY . .