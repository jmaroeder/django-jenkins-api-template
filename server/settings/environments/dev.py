"""
This file contains all the settings that defines the development server.

SECURITY WARNING: don't run with debug turned on in production!
"""

import logging

from server.settings.components.common import INSTALLED_APPS, MIDDLEWARE

# Setting the development status:

DEBUG = True

INSTALLED_APPS += ("nplusone.ext.django",)

MIDDLEWARE += ("querycount.middleware.QueryCountMiddleware",)

# nplusone
# https://github.com/jmcarp/nplusone

# Should be the first in line:
MIDDLEWARE = ("nplusone.ext.django.NPlusOneMiddleware",) + MIDDLEWARE  # noqa: WPS440

# Logging N+1 requests:
NPLUSONE_RAISE = True  # comment out if you want to allow N+1 requests
NPLUSONE_LOGGER = logging.getLogger("django")
NPLUSONE_LOG_LEVEL = logging.WARN

QUERYCOUNT = {
    "THRESHOLDS": {"MEDIUM": 50, "HIGH": 200, "MIN_TIME_TO_LOG": 0, "MIN_QUERY_COUNT_TO_LOG": 2},
}
