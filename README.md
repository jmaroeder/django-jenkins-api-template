# API

## Prerequisites

You will need:

- `python3.8` (see `pyproject.toml` for full version)
- `postgresql` with version `9.6`
- `docker` with [version at least](https://docs.docker.com/compose/compose-file/#compose-and-docker-compatibility-matrix) `18.02`

## Development

When developing locally, we use:

- [`editorconfig`](http://editorconfig.org/) plugin (**required**)
- [`poetry`](https://github.com/sdispater/poetry) (**required**)
- `pycharm 2017+` or `vscode`

## Getting Started

### Local development without Docker

It is not recommended to run the server outside of Docker, but it can be very helpful to be able for editor integration and to run the test/static analysis tools in a local `virtualenv`. To create a virtual environment, use poetry:

```console
# install the dependencies in a virtualenv
$ brew install openssl libpq  # (necessary to install psycopg2 python library)
$ export LDFLAGS="-L/usr/local/opt/openssl/lib"
$ export CPPFLAGS="-I/usr/local/opt/openssl/include" # necessary to compile psycopg2
$ poetry install
# activate the virtualenv
$ poetry shell
```

```console
$ git clone https://github.com/jmaroeder/django-starter.git
$ cd django-starter
$ poetry install
```


## Process

Before committing, run `script/pre-commit.sh` to automatically format code according to a standard style.

```console
$ scripts/pre-commit.sh
```

### Rationale
Static analysis tools are a useful tool to maintain consistent code and avoid common mistakes. To this end, a large number of tools are used as part of the CI workflow prior to running actual tests.

1. [flake8](http://flake8.pycqa.org/): multi-purpose static analysis tool with many plugins:
    - flake8-annotations-complexity
    - flake8-bandit
    - flake8-broken-line
    - flake8-bugbear
    - flake8-builtins
    - flake8-coding
    - flake8-commas
    - flake8-comprehensions
    - flake8-debugger
    - flake8-django
    - flake8-docstrings
    - flake8-eradicate
    - flake8-executable
    - flake8-isort
    - flake8-logging-format
    - flake8-pep3101
    - flake8-plugin-utils
    - flake8-polyfill
    - flake8-print
    - flake8-pytest
    - flake8-pytest-style
    - flake8-quotes
    - flake8-rst-docstrings
    - flake8-string-format
    - mccabe
    - pep8-naming
    - wemake-python-styleguide
1. [django-admin check --deploy](https://docs.djangoproject.com/en/2.2/ref/django-admin/#cmdoption-check-deploy): checks for common Django problems
1. [django-admin makemigrations --check](https://docs.djangoproject.com/en/2.2/ref/django-admin/#cmdoption-makemigrations-check): ensures all model migrations have been created
1. [xenon](https://xenon.readthedocs.io/): monitors code complexity
1. [poetry check](https://poetry.eustace.io/docs/cli/#check): ensures `pyproject.toml` is correct
1. [pip check](https://pip.pypa.io/en/stable/reference/pip_check/): ensures all installed dependencies are compatible


## Project Layout
### .
- `README.md` - main readme file, it specifies the entry point to the project's documentation
- `.dockerignore` - specifies what files should not be copied to the `docker` image
- `.editorconfig` - file with format specification. You need to install the required plugin for your IDE in order to enable it
- `.gitignore` - file that specifies what should we commit into the repository and we should not
- `docker-compose.yml` - this the file specifies `docker` services that are needed for development and testing
- `docker-compose.override.yml` - local override for `docker-compose`. Is applied automatically and implicitly when no arguments provided to `docker-compose` command
- `manage.py` - main file for your `django` project. Used as an entry point for the `django` project
- `pyproject.toml` - main file of the project. It defines the project's dependencies.
- `poetry.lock` - lock file for dependencies. It is used to install exactly the same versions of dependencies on each build
- `setup.cfg` - configuration file, that is used by all tools in this project
- `sql/` - helper folder, that contains `sql` script for database setup and teardown for local development

### ./api
**Primary app**

### ./server
- `server/urls.py` - `django` [urls definition](https://docs.djangoproject.com/en/3.0/topics/http/urls/)
- `server/wsgi.py` - `django` [wsgi definition](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface)
- `server/settings` - settings defined with `django-split-settings`, see this [tutorial](https://medium.com/wemake-services/managing-djangos-settings-e2b7f496120d) for more information

### tests
- `tests/conftest.py` - main configuration file for `pytest` runner
- `tests/test_server` - tests that ensures that basic `django` stuff is working, should not be removed
- `tests/test_api/` - folder for `api`-specific testst


## Container internals

We start containers with `tini`. Because this way we have a proper signal handling and eliminate zombie processes. Read the [official docs](https://github.com/krallin/tini) to know more.


## Other notes

This project was generated with a heavily modified version of [`wemake-django-template`](https://github.com/wemake-services/wemake-django-template). Current template version is: [1392938b1a370c8d79e811c572a4aff68996ec0e](https://github.com/wemake-services/wemake-django-template/tree/1392938b1a370c8d79e811c572a4aff68996ec0e). See what is [updated](https://github.com/wemake-services/wemake-django-template/compare/1392938b1a370c8d79e811c572a4aff68996ec0e...master) since then.
