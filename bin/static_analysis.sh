#!/usr/bin/env bash

set -o errexit
set -o nounset
set -x

: "${PYTHONPATH:=}"

flake8 .
PYTHONPATH="$PYTHONPATH:$PWD" mypy server api
ALLOWED_HOSTS=. DJANGO_ENV=prod ./manage.py check --deploy --fail-level WARNING
DB_URL=sqlite:///db.sqlite3 ./manage.py makemigrations --dry-run --check
xenon --max-absolute A --max-modules A --max-average A .
poetry check
pip check
yamllint --strict --format parsable .
