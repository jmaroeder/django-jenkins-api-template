#!/usr/bin/env bash

set -o errexit
set -o nounset
set -x

pytest --dead-fixtures --dup-fixtures --junitxml=
pytest
