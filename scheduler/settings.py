# -*- coding:utf-8 -*-
"""
Django settings for scheduler project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import mimetypes
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tn%*bt&f3#2d60+!&(or247877=w3j81!^k5e1&5$(5sh(jk0%'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
# TEMPLATE_DEBUG = DEBUG

# A list of strings representing the host/domain names that this Django site can serve.
# https://docs.djangoproject.com/en/1.8/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    '*',
]

# Celery settings
# http://docs.celeryproject.org/en/3.1/configuration.html

BROKER_URL = 'redis://localhost:6379/0'

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
# CELERY_TASK_RESULT_EXPIRES = 10
CELERY_RESULT_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
# CELERY_RESULT_BACKEND = 'djcelery.backends.cache:CacheBackend'  # django-celery cached database result backend
# CELERY_RESULT_BACKEND = "djcelery.backends.database:DatabaseBackend"  # django-celery database result backend
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
# CELERY_SEND_EVENTS = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',  # https://docs.djangoproject.com/en/1.11/ref/contrib/admin/
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djcelery',  #
    'apps',  #
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'scheduler.urls'

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

WSGI_APPLICATION = 'scheduler.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# 如果使用 CELERY_RESULT_BACKEND = 'djcelery.backends.cache:CacheBackend'
# 安装依赖 django-cache-extension
# CACHES = {
#     "default": {
#         'BACKEND': 'cache_extension.backends.redis.ExtensionRedisBackend',
#         'LOCATION': 'redis://localhost:6379/0',
#         'TIMEOUT': '172800',
#         "KEY_PREFIX": "cache_extension",
#         'OPTIONS': {
#             "DB": 0,
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#             'PARSER_CLASS': 'redis.connection.HiredisParser',
#             'PICKLE_VERSION': 2,
#         }
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Hong_Kong'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = 'static'
STATIC_URL = '/static/'

mimetypes.add_type("image/svg+xml", ".svg", True)
mimetypes.add_type("image/svg+xml", ".svgz", True)
