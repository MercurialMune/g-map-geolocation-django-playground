import os
import logging.config
from decouple import config, Csv
import dj_database_url
from django.contrib.messages import constants as messages


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = config( 'SECRET_KEY' )
MODE = config( "MODE", default="dev" )
LOGGING_CONFIG = None
LOGLEVEL = 'DEBUG'
DEBUG = config( 'DEBUG', default=False, cast=bool )

if config( 'MODE' ) == "dev":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': config( 'DB_NAME' ),
            'USER': config( 'DB_USER' ),
            'PASSWORD': config( 'DB_PASSWORD' ),
            'HOST': config( 'DB_HOST' ),
            'PORT': '',
        }
    }
else:
    DATABASES = {
        'default': dj_database_url.config(
            default=config( 'DATABASE_URL' )
        )
    }
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'default': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'logfile': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.FileHandler',
            'filename':  os.path.join( BASE_DIR, 'dev.log' ),
            'formatter': 'default'
        },

    },
    'loggers': {
        'workingcvapp': {
            'level': 'DEBUG',
            'handlers': ['console', 'logfile'],
            'propagate': False,
        },
        'ug': {
            'level': 'DEBUG',
            'handlers': ['console', 'logfile'],
            'propagate': False,
        },

    },
})
db_from_env = dj_database_url.config( conn_max_age=500 )
DATABASES['default'].update( db_from_env )
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "app",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

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


MESSAGE_TAGS = {
    messages.DEBUG: 'info',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Nairobi'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join( BASE_DIR, 'static' ),
)
STATIC_ROOT = os.path.join( BASE_DIR, 'staticfiles' )
MEDIA_ROOT = os.path.join( BASE_DIR, 'media' )
MEDIA_URL = '/media/'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = 'home'
LOGIN_REDIRECT_URL = 'home'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
