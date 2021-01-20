"""
Local settings
"""

import os
from .common import *

DEBUG = os.environ.get("DJANGO_DEBUG", default=True)


# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY", default="x01&d4r=bb6m+4(quhnts7e3+qhlk1b&6z_p%5u(jvuz*-1$=r"
)

ALLOWED_HOSTS = ["*"]
