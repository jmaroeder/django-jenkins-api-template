#!/usr/bin/env bash

set -o errexit
set -o nounset
set -x

poetry run black .

export COMPOSE_FILE=docker-compose.yml:docker-compose.ci.yml
export COMPOSE_PROJECT=api-pre-commit
docker-compose build web
docker-compose run --no-deps --rm web bin/static_analysis.sh
docker-compose up -d db
docker-compose run --rm wait
docker-compose run --rm web bin/test.sh
