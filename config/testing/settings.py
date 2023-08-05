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
ALLOWED_HOSTS = ['*']

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': '',
    }
}

EMAIL_HOST = env('EMAIL_HOST', default='mailhog')
EMAIL_PORT = 1025
