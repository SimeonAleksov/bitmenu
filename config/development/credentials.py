DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': 'bitmenu',
        'USER': 'PCYfBuNREvMRNnaduVQoaFTzviAWDKuD',
        'PASSWORD': 'Y8hoMldr6CZMQFlFvTkMPCplJdF6t6ctstldVvluwALWsPvRaeORnnz3Y81JybTO',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

DATABASES['default']['ATOMIC_REQUESTS'] = True

REDIS_URL = 'redis://redis:6379/0'
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = CELERY_BROKER_URL

CELERY_FLOWER_USER = 'MajPNicudFvptcwYSdIEOwdnzSLBjqBx'
CELERY_FLOWER_PASSWORD = 'd1tJoPrIOp3KtXt2OJNSnbtt54LCR08kVttQQFlTsrBRwrP6yMRe2AAUeJ8qQnKj'

STRIPE_TEST_PUBLIC_KEY = '<TAG>'
STRIPE_TEST_SECRET_KEY = '<TAG>'
STRIPE_LIVE_MODE = False
DJSTRIPE_WEBHOOK_SECRET = '<TAG>'
