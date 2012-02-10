# Django settings for carlog project.

import os

APP_BASE_DIR = os.path.abspath(os.path.dirname( globals()[ '__file__' ] )) 
APP_PARENT_DIR = os.path.dirname(APP_BASE_DIR)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'carlog_db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = ''

MEDIA_URL = ''

STATIC_ROOT = ''

STATIC_URL = os.path.join(APP_PARENT_DIR, 'static')

ADMIN_MEDIA_PREFIX = os.path.join(STATIC_URL, 'admin/')

STATICFILES_DIRS = (STATIC_URL,
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = '%&nlm&53x!xw()oq-to%y_krr-n$_j9w3c8nu4b935axmljixo'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'carlog.urls'

TEMPLATE_DIRS = (os.path.join(APP_BASE_DIR, 'templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'socialregistration',
    'socialregistration.contrib.facebook',
    'socialregistration.contrib.twitter',
    'carlog.fangorn',
    'carlog.entries',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
        'socialregistration.contrib.facebook.auth.FacebookAuth',
        'socialregistration.contrib.twitter.auth.TwitterAuth',
)

LOGIN_URL          = '/accounts/login-page/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL    = '/accounts/login/'

FACEBOOK_APP_ID = '298823853479572'
FACEBOOK_SECRET_KEY = 'ae44fc452df4c392d224f7f6ad4ed5f7'
FOURSQUARE_REQUEST_PERMISSIONS = ''

TWITTER_CONSUMER_KEY = 'MQW7d3rfHcey3TKK7Ajdw'
TWITTER_CONSUMER_SECRET_KEY = 'NQnsklJyOE2XyrOfhNq2yrsU7ZnORBs3sc7DpiYnV7k'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
