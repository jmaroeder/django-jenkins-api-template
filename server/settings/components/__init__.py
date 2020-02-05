# Shared components

import csv
from typing import Sequence

import environ


def csv_converter(line: str) -> Sequence[str]:
    """Parses a single csv line into an array of strings."""
    return next(csv.reader([line]))


@environ.config(prefix="")
class Config:
    """Custom Config class."""

    allowed_hosts = environ.var("*", converter=csv_converter)
    db_url = environ.var("sqlite:///db.sqlite3")  # default allows for running manage.py locally
    debug = environ.bool_var(False)
    django_env = environ.var("local")
    secret_key = environ.var("default-secret-key")

    @environ.config
    class RestFramework:
        parser_classes = environ.var("rest_framework.parsers.JSONParser", converter=csv_converter)
        renderer_classes = environ.var(
            "rest_framework.renderers.JSONRenderer", converter=csv_converter,
        )

    drf: RestFramework = environ.group(RestFramework)


config: Config = Config.from_environ()  # type: ignore
