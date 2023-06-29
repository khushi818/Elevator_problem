from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': os.environ.get('PASSWORD'),
        'HOST': 'containers-us-west-188.railway.app',
        'PORT': '7818',
    }
}

ALLOWED_HOSTS = ['localhost', 'containers-us-west-188.railway.app']
