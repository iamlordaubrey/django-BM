"""
WSGI config for cis_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cis_api.settings")

application = Cling(get_wsgi_application())
