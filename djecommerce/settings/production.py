from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# [START dbconfig]

# The following DATABASES configuration is for PostgreSQL. If you are using
# MySQL, use the commented-out block that follows this one instead. In this
# case, please also follow the commented instructions in requirements.txt.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nashasdb',
        'USER': 'nashasuserdb',
        'PASSWORD': 'holamundo',
        'PORT': '5432',
    }
}

# Uncomment this DATABASES block and use it instead of the above if you are
# using MySQL. Also follow the commented instructions in requirements.txt.

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'polls',
#         'USER': '<your-database-user>',
#         'PASSWORD': '<your-database-password>',
#         'PORT': '3306',
#     }
# }

# In the flexible environment, you connect to CloudSQL using a unix socket.
# Locally, you can use the CloudSQL proxy to proxy a localhost connection
# to the instance
DATABASES['default']['HOST'] = '/cloudsql/testflexnasha:us-central1:nashasinstance'
if os.getenv('GAE_INSTANCE'):
    pass
else:
    DATABASES['default']['HOST'] = '127.0.0.1'
# [END dbconfig]

# Use a in-memory sqlite3 database when testing in CI systems
if os.getenv('TRAMPOLINE_CI', None):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
        }
    }


