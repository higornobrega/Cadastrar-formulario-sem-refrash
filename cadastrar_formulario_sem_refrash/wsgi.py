"""
WSGI config for cadastrar_formulario_sem_refrash project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cadastrar_formulario_sem_refrash.settings')

application = get_wsgi_application()
