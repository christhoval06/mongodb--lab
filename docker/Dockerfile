# Pull official base image 
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONIOENCODING=utf-8

RUN apt-get update \
    && apt-get install -y gcc python3-dev musl-dev libmagic1 libffi-dev netcat-traditional \
    build-essential libpq-dev 

COPY pyproject.toml /app/

RUN pip3 install poetry
# Install dependencies
RUN poetry install

# Copy entrypoint.sh
COPY ./docker/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

COPY . /app/

# create unprivileged user
# RUN adduser --disabled-password --gecos '' myuser

ENTRYPOINT [ "/entrypoint.sh" ]
