#!/usr/bin/env bash

set -o errexit
set -o nounset
set -x

export COMPOSE_PROJECT=api-watch
docker-compose build web
docker-compose up -d db
docker-compose run --rm wait
docker-compose run --rm web ptw -c
