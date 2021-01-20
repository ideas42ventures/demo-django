"""
Local settings
"""

import os
from .common import *

ALLOWED_HOSTS = ["studio-demo-django.herokuapp.com"]

# Static Assets
# ------------------------
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
