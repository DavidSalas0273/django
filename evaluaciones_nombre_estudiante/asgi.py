import os

from django.core.asgi import get_asgi_application

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'evaluaciones_nombre_estudiante.settings',
)

application = get_asgi_application()
