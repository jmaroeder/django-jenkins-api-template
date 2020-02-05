#!/usr/bin/env bash

set -o errexit
set -o nounset
set -x

docker-compose rm --force --stop -v
