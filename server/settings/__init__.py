"""
This is a django-split-settings main file.

For more information read this:
https://github.com/sobolevn/django-split-settings
"""

import os
from pathlib import PurePath

from split_settings.tools import include

BASE_DIR = PurePath(__file__).parent.parent.parent

ENV = os.environ.get("DJANGO_ENV", "dev")

include(
    "components/*.py", f"environments/{ENV}.py",
)
