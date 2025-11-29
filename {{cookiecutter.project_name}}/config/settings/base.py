# --- base.py ---
{% if cookiecutter.use_sentry.lower() == 'y' %}
import sentry_sdk
{% endif %}
from pathlib import Path
from decouple import config
from core.utils.features import get_enabled_apps, is_feature_enabled
{% if cookiecutter.use_sentry.lower() == 'y' %}
from sentry_sdk.integrations.django import DjangoIntegration
{% endif %}

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = config('SECRET_KEY', 'change-me')
DEBUG = config('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = config('ALLOWED_HOSTS', '*').split(',')

BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
]

DYNAMIC_APPS = get_enabled_apps()

if is_feature_enabled("drf_spectacular"):
    BASE_APPS += ['drf_spectacular']

INSTALLED_APPS = BASE_APPS + DYNAMIC_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_DEFAULT_NAME'),
        'USER': config('DB_DEFAULT_USER'),
        'PASSWORD': config('DB_DEFAULT_PASSWORD'),
        'HOST': config('DB_DEFAULT_HOST'),
        'PORT': config('DB_DEFAULT_PORT'),
    },
    'analytics': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_ANALYTICS_NAME'),
        'USER': config('DB_ANALYTICS_USER'),
        'PASSWORD': config('DB_ANALYTICS_PASSWORD'),
        'HOST': config('DB_ANALYTICS_HOST'),
        'PORT': config('DB_ANALYTICS_PORT'),
    },
}

DATABASE_ROUTERS = ['core.db_router.DatabaseRouter']

STATIC_URL = 'static/'

MEDIA_URL = "media"
MEDIA_ROOT = BASE_DIR / "media"

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema'
}

AUTH_USER_MODEL = 'users.User'

# JWT Config
JWT_SECRET = SECRET_KEY
JWT_ALGORITHM = config('JWT_ALGORITHM', 'HS256')
JWT_EXP_DELTA_SECONDS = config('JWT_EXP_DELTA_SECONDS', 3600)

# Swagger Config
SPECTACULAR_SETTINGS = {
    'TITLE': "{{ cookiecutter.project_name }}",
    'DESCRIPTION': 'API documentation for the enterprise project',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}

{% if cookiecutter.use_celery.lower() == 'y' %}
# Celery Configuration
CELERY_BROKER_URL = f"redis://{config('REDIS_HOST', 'localhost')}:{config('REDIS_PORT', 6379)}/0"
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = '{{ cookiecutter.timezone }}'
{% endif %}
{% if cookiecutter.use_sentry.lower() == 'y' %}
SENTRY_DSN = config("SENTRY_DSN", "")

if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[DjangoIntegration()],
        traces_sample_rate=1.0,
        send_default_pii=True,
    )
{% endif %}
