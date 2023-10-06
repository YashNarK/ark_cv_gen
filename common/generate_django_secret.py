from django.core.management.utils import get_random_secret_key


def generate_django_secret():
    return 'django-insecure-'+get_random_secret_key()