from config.settings_base import env

DATABASES = {'default': env.db('DATABASE_URL', engine='django_tenants.postgresql_backend')}

DATABASES['default']['ATOMIC_REQUESTS'] = True

REDIS_URL = 'redis://redis:6379/0'

CELERY_BROKER_URL = env('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = CELERY_BROKER_URL

CELERY_FLOWER_USER = 'MajPNicudFvptcwYSdIEOwdnzSLBjqBx'
CELERY_FLOWER_PASSWORD = 'd1tJoPrIOp3KtXt2OJNSnbtt54LCR08kVttQQFlTsrBRwrP6yMRe2AAUeJ8qQnKj'
