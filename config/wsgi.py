"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
>>>>>>> 13f530bebb75fa9b6b6a3f778aa47d0c7a4c9cc9

application = get_wsgi_application()
