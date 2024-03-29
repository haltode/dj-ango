from .common import * # noqa


DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
# You can generate a key using the following command:
# openssl rand -base64 64 | sed "s/[/10lO#+=]//g" | tr -d "\n"; echo
SECRET_KEY = 'CHANGEME'

YOUTUBE_API_KEY = 'CHANGEME'

ALLOWED_HOSTS = ['127.0.0.1', '::1', 'localhost']
SITE_HOST = 'localhost:8000'

STATIC_ROOT = '/path/to/static/dir'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cisco',
    }
}
