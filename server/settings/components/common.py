"""Django settings."""

from typing import Tuple

import dj_database_url

from server.settings.components import config

# Application

ALLOWED_HOSTS = config.allowed_hosts
APPEND_SLASH = False
INSTALLED_APPS: Tuple[str, ...] = (
    "api.apps.ApiConfig",
    "server.live.apps.LiveConfig",
    "django.contrib.contenttypes",
)
MIDDLEWARE: Tuple[str, ...] = (
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
)
PREPEND_WWW = False
ROOT_URLCONF = "server.urls"
SECRET_KEY = config.secret_key
SILENCED_SYSTEM_CHECKS = [
    "security.W002",
    "security.W003",
    "security.W004",
    "security.W008",
    "security.W009",
    "security.W022",
]
WSGI_APPLICATION = "server.wsgi.application"


# Database

DATABASES = {
    "default": dj_database_url.parse(config.db_url),
}


# Internationalization

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True
