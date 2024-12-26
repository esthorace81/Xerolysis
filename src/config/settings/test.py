from django.core.management.utils import get_random_secret_key

from .base import *  # noqa: F403

SECRET_KEY = get_random_secret_key()
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',  # Base de datos en memoria
    }
}
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',  # Hashing rápido para tests
]
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'  # No envía mails reales
