# define an alias for the specific python version used in this file.
FROM python:3.11.4-slim-bullseye as python

# Python build stage
FROM python as python-build-stage

ARG BUILD_ENVIRONMENT=local

# Install apt packages
RUN apt-get update && apt-get install --no-install-recommends -y \
  # dependencies for building Python packages
  build-essential \
  # psycopg2 dependencies
  libpq-dev

# Requirements are installed here to ensure they will be cached.
COPY ./requirements .

# Create Python Dependency and Sub-Dependency Wheels.
RUN pip wheel --wheel-dir /usr/src/app/wheels  \
  -r ${BUILD_ENVIRONMENT}.txt


# Python 'run' stage
FROM python as python-run-stage

ARG BUILD_ENVIRONMENT=local
ARG APP_HOME=/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}


# devcontainer dependencies and utils
RUN apt-get update && apt-get install --no-install-recommends -y \
  sudo git bash-completion nano ssh

# Create devcontainer user and add it to sudoers
RUN groupadd --gid 1000 dev-user \
  && useradd --uid 1000 --gid dev-user --shell /bin/bash --create-home dev-user \
  && echo dev-user ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/dev-user \
  && chmod 0440 /etc/sudoers.d/dev-user


# Install required system dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
  # psycopg2 dependencies
  libpq-dev \
  # Translations dependencies
  gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# All absolute dir copies ignore workdir instruction. All relative dir copies are wrt to the workdir instruction
# copy python dependency wheels from python-build-stage
COPY --from=python-build-stage /usr/src/app/wheels  /wheels/

# use wheels to install python dependencies
RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
  && rm -rf /wheels/

COPY ./compose/production/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start



# copy application code to WORKDIR
COPY . ${APP_HOME}

ENTRYPOINT ["/entrypoint"]






# FROM alpine:3.18

# ENV PYTHONUNBUFFERED 1

# # Set timezone
# RUN apk add --no-cache tzdata \
#     && echo "UTC" > /etc/timezone \
#     && ln -sf /usr/share/zoneinfo/UTC /etc/localtime

# # Install system dependencies
# RUN apk update && apk upgrade \
#     && apk add --no-cache python3 python3-dev py3-pip libpq mysql-client gcc musl-dev \
#     && pip install --upgrade pip

# # Set the working directory
# WORKDIR /app

# # Copy the project files into the container
# COPY ./requirements.txt /app/requirements.txt

# # Install project dependencies
# RUN pip install -r requirements.txt

# # Copy the rest of the project files into the container
# COPY . /app

# # Create necessary directories and set permissions
# RUN mkdir -p /vol/web/static \
#     && mkdir -p /vol/web/media \
#     && mkdir -p /vol/web/logs \
#     && chmod -R 755 /vol

# # Copy the start script and make it executable
# COPY ./scripts/start /start
# RUN sed -i 's/\r$//g' /start
# RUN chmod +x /start
