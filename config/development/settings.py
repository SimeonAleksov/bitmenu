from config import settings_base
from config.settings_base import env

for setting in dir(settings_base):
    if setting == setting.upper():
        globals()[setting] = getattr(settings_base, setting)

DEBUG = True
SECRET_KEY = env(
    'DJANGO_SECRET_KEY',
    default='UezwPFLUPHFvaEEqzdz0FYzO0wrmwnZWzmSHheisOmPyFbhNxxKzfbEnJW9cLgv6',
)
ALLOWED_HOSTS = ['localhost', '0.0.0.0', '127.0.0.1']

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': '',
    }
}

EMAIL_HOST = env('EMAIL_HOST', default='mailhog')
EMAIL_PORT = 1025

# pylint: disable=used-before-assignment
INSTALLED_APPS = ['whitenoise.runserver_nostatic'] + INSTALLED_APPS  # noqa: F821

INTERNAL_IPS = ['127.0.0.1', '10.0.2.2']

INSTALLED_APPS += ['django_extensions']  # noqa: F405

CELERY_TASK_EAGER_PROPAGATES = True
