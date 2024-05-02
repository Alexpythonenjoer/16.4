"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import logging
from logging.handlers import SMTPHandler
from django.conf import settings
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-u9q9j#xx_r$h=i4l)ed9p2c5#_+2biw%pj^8fnmy-v^o9aidgv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'news',
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_apscheduler'

]
DEFAULT_FROM_EMAIL='ps4123303@yandex.ru'
SITE_ID=1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
]

ROOT_URLCONF = 'project.urls'
# os.path.join(BASE_DIR, 'template')
# import os
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
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]
WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DEFAULT_FROM_EMAIL = 'EMAIL_HOST_USER'+'@yandex.ru'

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'ps4123303'
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_SSL = True

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

class DebugFilter(logging.Filter):
    def filter(self, record):
        return settings.DEBUG

class ProductionFilter(logging.Filter):
    def filter(self, record):
        return not settings.DEBUG

# Console logging when DEBUG is True
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.addFilter(DebugFilter())
console_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s - %(pathname)s - %(exc_info)s')
console_handler.setFormatter(console_format)

# General logging to file when DEBUG is False
general_handler = logging.FileHandler('general.log')
general_handler.setLevel(logging.INFO)
general_handler.addFilter(ProductionFilter())
general_format = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(message)s')
general_handler.setFormatter(general_format)

# Error logging to file
error_handler = logging.FileHandler('errors.log')
error_handler.setLevel(logging.ERROR)
error_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s - %(pathname)s')
error_handler.setFormatter(error_format)

# Security logging to file
security_handler = logging.FileHandler('security.log')
security_handler.setLevel(logging.WARNING)
security_format = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(message)s')
security_handler.setFormatter(security_format)

# Mail logging for errors when DEBUG is False
mail_handler = SMTPHandler(  # Fill this with your mail server settings
    mailhost=("mailhost.com", 587),
    fromaddr="from@example.com",
    toaddrs=["to@example.com"],
    subject="Django Error",
)
mail_handler.setLevel(logging.ERROR)
mail_handler.addFilter(ProductionFilter())
mail_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s - %(pathname)s')
mail_handler.setFormatter(mail_format)

loggers = {
    "django": {
        "handlers": ["console_handler", "general_handler"],
        "level": "DEBUG",
    },
    "django.request": {
        "handlers": ["error_handler", "mail_handler"],
        "level": "ERROR",
    },
    "django.server": {
        "handlers": ["error_handler", "mail_handler"],
        "level": "ERROR",
    },
    "django.template": {
        "handlers": ["error_handler"],
        "level": "ERROR",
    },
    "django.db.backends": {
        "handlers": ["error_handler"],
        "level": "ERROR",
    },
    "django.security": {
        "handlers": ["security_handler"],
        "level": "WARNING",
    },
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console_handler": console_handler,
        "general_handler": general_handler,
        "error_handler": error_handler,
        "security_handler": security_handler,
        "mail_handler": mail_handler,
    },
    "loggers": loggers,
}
