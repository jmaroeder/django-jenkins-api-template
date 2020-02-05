#!/usr/bin/env bash

set -o errexit
set -o nounset
set -x

docker-compose up -d db
docker-compose run --rm wait
docker-compose up web
