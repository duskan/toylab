"""
WSGI config for toylab project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'toylab.settings')

application = get_wsgi_application()

# try:
    # from whitenoise.django import DjangoWhiteNoise
    # application = DjangoWhiteNoise(application)
# except ImportError:
    # pass
