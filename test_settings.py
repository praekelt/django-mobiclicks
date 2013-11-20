DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mobiclicks.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'mobiclicks.middleware.MobiClicksMiddleware',
)

INSTALLED_APPS = (
    'mobiclicks',
    'djcelery',
    'kombu.transport.django',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
)

CELERY_ALWAYS_EAGER = True
BROKER_URL = 'django://'
CELERY_RESULT_BACKEND = "database"

MOBICLICKS = {
    'CPA_SECURITY_TOKEN': 'foo',
    'TRACK_REGISTRATIONS': False,
    'CONFIRM_CLICKS': False,
}

import djcelery
djcelery.setup_loader()
