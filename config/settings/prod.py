"""
Django settings for {{ project_name }} project in production mode

This fill will be automatically used when using a dedicated application server.
See `base.py` for basic settings.

For the full list of settings and their values, see
https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/
"""


from .base import *


DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "78a1373acb9a08d3a6b773dab1590ed0e7185a3d5334e31ad9"

# remember to set this to your expected hostnames
ALLOWED_HOSTS = ['*','ia.bittito.com']
