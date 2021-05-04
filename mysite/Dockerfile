# pull official base image
FROM ubuntu:20.04

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies

RUN apt-get update && apt-get install -y \
    python3-pip
COPY ./requirements.txt /usr/src/app/requirements.txt
# RUN apt-get --no-cache --virtual .build-deps gcc libc-dev libxslt-dev && \
#     apt-get --no-cache libxslt && \
#     pip install --no-cache-dir lxml>=4.6.3 && \
#     apt-del .build-deps
RUN pip3 install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# copy project
COPY . /usr/src/app/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]