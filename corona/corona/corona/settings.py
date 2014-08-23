"""
Django settings for corona project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# # Connect to MongoDB and the real database

DB_NAME = 'corona'

from mongoengine import connect
connect( DB_NAME, host='mongodb://localhost:27017')

# # Use MongoDB Backend
# AUTHENTICATION_BACKENDS = (
#     'mongoengine.django.auth.MongoEngineBackend',
# )

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h(uc0mw8wfd_5c1jp(larvtmoau^)aghuvt_7shx+1iisq&*o3'

ACTIVATE_KEY = 'w8wfd_5clarvtmHIXQ$@h1jph(uc0m(x+1iisq&*o3^)aghuvt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Push Notification
APNS_ALIAS = ''
APNS_CERT_ALIAS = ''

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_rq',
    'django_rq_dashboard',
    'ws4redis',
    'redisboard',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
)

ROOT_URLCONF = 'corona.urls'

WSGI_APPLICATION = 'corona.wsgi.application'

#CORS Setting
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = ('GET', 'POST', 'PUT', 'DELETE')
CORS_ALLOW_CREDENTIALS = True

# # Database
# # https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Redis Cache Setup

CACHES = {
    # act as memcache
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': '127.0.0.1:6379:0',
        'OPTIONS': {
            'PASSWORD': '',  # Optional
            'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
            'PARSER_CLASS': 'redis.connection.HiredisParser',
            'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
            'CONNECTION_POOL_CLASS_KWARGS': {
                'max_connections': 500,
                'timeout': 10,
            }
        }
    },
}

DEFAULT_CACHE_ALIAS = 'default'

# SESSION_ENGINE = 'redis_sessions.session'
# SESSION_REDIS_HOST = '127.0.0.1'
# SESSION_REDIS_PORT = 6379
# SESSION_REDIS_DB = 1
# SESSION_REDIS_PASSWORD = ''
# SESSION_REDIS_PREFIX = 'session'

# Rest Framework Authentication

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework.authentication.BasicAuthentication',
#         'rest_framework.authentication.SessionAuthentication',
#     )
# }

# HTTPS Setup

# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

SESSION_COOKIE_AGE = 60*60*72

# Redis Queue

RQ_QUEUES = {
    'TEST': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 2,
        'PASSWORD': '',
    }
}

# RQ Dashboard

RQ = {
    'host': 'localhost',
    'port': 6379,
    'db': 2,
    'password': None,
}


# Logger Setup

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        }
    },
    'handlers': {
        'general_handler': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
            'formatter': 'verbose'
        },
        
    },
    'loggers': {
        'general': {
            'handlers':['general_handler'],
            'propagate': True,
            'level':'DEBUG',
        },
    }
}

# WebSocket
WEBSOCKET_URL = '/ws/'

WS4REDIS_CONNECTION = {
    'host': '127.0.0.1',
    'port': 6379,
    'db': 10,
    'password': '',
}

WS4REDIS_EXPIRE = 60*5
WS4REDIS_PREFIX = 'ws'

# DEV NEEDED !!! REMOVE IN PRODUCTION
WSGI_APPLICATION = 'ws4redis.django_runserver.application'

# EMAIL SETUP

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_ACCOUNT = 'welcome@appliters.com'
SMTP_PASSWORD = '123zxcvbnm'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
