"""
This file contains all the settings used in production.

This file is required and if dev.py is present these
values are overridden.
"""

from server.settings.components.common import ALLOWED_HOSTS

# Production flags:

DEBUG = False

if "*" in ALLOWED_HOSTS:
    raise Exception("prod environment must not allow `*` in ALLOWED_HOSTS!")
