# This Dockerfile uses multi-stage build to customize dev, ci, and prod images:
# https://docs.docker.com/develop/develop-images/multistage-build/

FROM python:3.8-alpine as base_build

ENV \
  # python:
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  # pip:
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  # poetry:
  POETRY_VERSION=1.0.3 \
  # path
  PATH="/usr/src/app/bin:${PATH}"

RUN \
  apk --no-cache add \
    bash \
    build-base \
    curl \
    gettext \
    git \
    libffi-dev \
    linux-headers \
    openssl \
    musl-dev \
    postgresql-dev \
    tini \
  && pip install -U "pip<20.0" \
  && pip install "poetry==$POETRY_VERSION"

WORKDIR /usr/src/app
COPY ./poetry.lock ./pyproject.toml /usr/src/app/

ENTRYPOINT ["/sbin/tini", "--", "docker-entrypoint.sh"]
CMD ["gunicorn.sh"]

HEALTHCHECK --interval=30s --timeout=5s \
  CMD curl --fail http://localhost:${GUNICORN_PORT:-8000}/live || exit 1

# skip dev dependencies
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-dev


##########################################
# dev build: for running local development
##########################################
FROM base_build as dev_build

# install dev dependencies
RUN poetry install --no-interaction


################################
# ci build: for running ci tests
################################
FROM dev_build as ci_build
COPY . /usr/src/app


######################################
# deployable build: for running in gcp
######################################
FROM base_build as deployable_build
COPY . /usr/src/app
