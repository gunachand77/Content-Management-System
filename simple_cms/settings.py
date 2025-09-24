import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Security - use environment variables in production
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-simple-cms-key-123')
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# CSRF settings
CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1:8000',
    'http://localhost:8000',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cms_app',
]

# Admin customization should come after INSTALLED_APPS
from django.contrib import admin

class CustomAdminSite(admin.AdminSite):
    site_header = "My Awesome Blog Administration"
    site_title = "My Awesome Blog Administration Admin"
    index_title = "Welcome to My Awesome Blog  Admin Portal"

custom_admin_site = CustomAdminSite(name='custom_admin')
admin.site = custom_admin_site

# Admin styling (you'll need to implement the context processor)
ADMIN_STYLE = '''
<style>
    body { font-size: 16px !important; }
    #header { background: #4f46e5 !important; }
    .module h2 { background: #6366f1 !important; }
    .selector-chosen h2 { background: #10b981 !important; }
</style>
'''

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'simple_cms.urls'

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

WSGI_APPLICATION = 'simple_cms.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # For production

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'