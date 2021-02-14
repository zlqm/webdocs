import os

from django.urls import path, re_path
from django.core import management

from . import docs, views

urlpatterns = [
    path('pets', views.PetsView.as_view()),
    path('pets/<int:pet_id>', views.PetView.as_view()),
    re_path(r'pets/(?P<pet_id>\d+)/images', views.PetImageView.as_view()),
]


def pytest_configure():
    import django
    from django.conf import settings

    settings.configure(
        ALLOWED_HOSTS='*',
        DEBUG_PROPAGATE_EXCEPTIONS=True,
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:'
            }
        },
        SITE_ID=1,
        SECRET_KEY='not very secret in tests',
        STATIC_URL='/static/',
        ROOT_URLCONF=__name__,
        TEMPLATE_LOADERS=(
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ),
        MIDDLEWARE=(
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
            'simple_django_api.jwt.middleware.AuthenticationMiddleware',
        ),
        INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.sites',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'webdocs.django',
        ),
        PASSWORD_HASHERS=('django.contrib.auth.hashers.MD5PasswordHasher', ),
        OPENAPI_VERSION=docs.OPENAPI_VERSION,
        OPENAPI_INFO=docs.OPENAPI_INFO,
        OPENAPI_EXTERNALDOCS=docs.OPENAPI_EXTERNALDOCS,
        OPENAPI_TAGS=docs.OPENAPI_TAGS,
        OPENAPI_COMPONENTS=docs.OPENAPI_COMPONENTS,
    )

    import django
    django.setup()
