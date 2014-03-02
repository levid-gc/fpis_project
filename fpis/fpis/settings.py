# -*- coding: utf-8 -*-
"""
Django settings for fpis project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
reload(sys)
sys.setdefaultencoding('gbk')


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SITE_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')


STATIC_ROOT = os.path.join(SITE_ROOT, 'static')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wxm@++4&n#^xprsmisdz90mu=u2_@048qpu)$^%k96@*6n*jlr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

LOGIN_REDIRECT_URL = '/login/'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'levid.gc@gmail.com'
EMAIL_HOST_PASSWORD = '******'

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER


# Application definition

# Django-REST-Framework


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django-groundwork',
    'xadmin',
    'crispy_forms',
    'reversion',
    'rest_framework',
    'account',
    'schedule',
    'attendance',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


ROOT_URLCONF = 'fpis.urls'

WSGI_APPLICATION = 'fpis.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',      # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'fpis',                            # Or path to database file if using sqlite3.
        'USER': 'root',                            # Not used with sqlite3.
        'PASSWORD': '******',                # Not used with sqlite3.
        'HOST': 'localhost',                       # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                            # Set to empty string for default. Not used with sqlite3.
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    ("css", os.path.join(STATIC_ROOT, 'css')),
    ("js", os.path.join(STATIC_ROOT, 'js')),
    ("images", os.path.join(STATIC_ROOT, 'images')),
    ("bootstrap", os.path.join(STATIC_ROOT, 'bootstrap')),
    ("xadmin", os.path.join(STATIC_ROOT, 'xadmin')),
    #os.path.join(HERE,'static').replace('\\','/'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

#templates files根目录下加载
TEMPLATE_DIRS = (os.path.join(BASE_DIR,'templates'),)
# List of callables that know how to import templates from various sources.

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)







import os
TEMPLATE_DIRS += (os.path.join( os.path.dirname(__file__), 'templates') ,)
