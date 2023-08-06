import os
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

STRIPE_TEST_PUBLIC_KEY = '<TAG>'
STRIPE_TEST_SECRET_KEY = '<TAG>'
STRIPE_LIVE_MODE = False
DJSTRIPE_WEBHOOK_SECRET = '<TAG>'
