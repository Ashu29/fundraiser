"""
WSGI config for fundraiser project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from fundraiser.utils import get_default_django_settings_module

os.environ.setdefault("DJANGO_SETTINGS_MODULE", get_default_django_settings_module())

application = get_wsgi_application()
