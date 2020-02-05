#!/usr/bin/env bash

set -o errexit
set -o nounset

echo "ENV is $DJANGO_ENV"

# Defaults
: "${GUNICORN_PORT:=8000}"
: "${GUNICORN_RELOAD:=1}"
: "${GUNICORN_WORKERS:=4}"

# Start gunicorn
set -x
exec "/usr/local/bin/gunicorn" \
  "--workers=$GUNICORN_WORKERS" \
  "$([ $GUNICORN_RELOAD != 0 ] && echo '--reload' )" \
  "--bind=0.0.0.0:$GUNICORN_PORT" \
  "--chdir=/usr/src/app" \
  "--log-file=-" \
  "--worker-tmp-dir=/dev/shm" \
  "server.wsgi:application"
