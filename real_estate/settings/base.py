import logging
import logging.config
from datetime import timedelta
from pathlib import Path

import environ
from django.utils.log import DEFAULT_LOGGING

# Setting up environment variables using the 'django-environ' package
env = environ.Env(DEBUG=(bool, False))  # DEBUG will be a boolean, default is False

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Load environment variables from the .env file
environ.Env.read_env(BASE_DIR / ".env")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

# Hosts that are allowed to access the project
ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(" ")


# Application definition

DJANGO_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
]

# Refers to the default site in the django_site database table
SITE_ID = 1

THIRD_PARTY_APPS = [
    "rest_framework",  # For building REST APIs
    "django_filters",  # Filtering for Django REST Framework
    "django_countries",  # Country field for models
    "phonenumber_field",  # Phone number fields
    "djoser",  # User management (registration, password reset, etc.)
    "rest_framework_simplejwt",  # JWT-based authentication
    "djcelery_email"  # Email sending with Celery for asynchronous email delivery
]

LOCAL_APPS = [
    "apps.common",
    "apps.users",
    "apps.profiles",
    "apps.ratings",
    "apps.properties",
    "apps.enquiries",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# The root URL configuration for the project
ROOT_URLCONF = "real_estate.urls"

# Template engine settings (used for rendering HTML templates)
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # Directories for custom templates
        "APP_DIRS": True,  # Look for templates inside app directories
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "real_estate.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Africa/Kigali"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# URLs and directories for static and media files
STATIC_URL = "/staticfiles/"
STATIC_ROOT = BASE_DIR / "staticfiles"  # Where collected static files will go
STATICFILES_DIR = []  # Extra directories for static files

MEDIA_URL = "/mediafiles/"
# Where user-uploaded files (like profile pictures) are stored
MEDIA_ROOT = BASE_DIR / "mediafiles"


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Custom user model (defined in apps.users)
AUTH_USER_MODEL = "users.User"

# REST Framework settings
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    )
}

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": (
        "Bearer",
        "JWT",
    ),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=120),  # Token lifetime
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),  # Refresh token lifetime
    "SIGNING_KEY": env("SIGNING_KEY"),  # Key for signing tokens
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",  # Where to look for the token in the request headers
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
}

# Djoser is a Django app that provides a set of RESTful endpoints for user authentication and management.
# It simplifies the process of handling user registration, login, password resets, and account activation.
DJOSER = {
    "LOGIN_FIELD": "email",  # Users log in using their email
    "USER_CREATE_PASSWORD_RETYPE": True,  # Require password confirmation during registration
    "USERNAME_CHANGED_EMAIL_CONFIRMATION": True,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    "SEND_CONFIRMATION_EMAIL": True,  # Sends a confirmation email after certain actions, like registration
    "PASSWORD_RESET_CONFIRM_URL": "password/reset/confirm/{uid}/{token}",
    "SET_PASSWORD_RETYPE": True,
    "PASSWORD_RESET_CONFIRM_RETYPE": True,
    "USERNAME_RESET_CONFIRM_URL": "email/reset/confirm/{uid}/{token}",
    "ACTIVATION_URL": "activate/{uid}/{token}",  # URL for account activation
    "SEND_ACTIVATION_EMAIL": True,  # Send activation email after registration
    # Custom serializers for user operations
    "SERIALIZERS": {
        "user_create": "apps.users.serializers.CreateUserSerializer",  # Serializer for new user creation
        "user": "apps.users.serializers.UserSerializer",  # Serializer for retrieving user info
        "current_user": "apps.users.serializers.UserSerializer",  # Serializer for current user's info
        "user_delete": "djoser.serializers.UserDeleteSerializer",  # Serializer for user deletion
    },
}

# Logging settings
logger = logging.getLogger(__name__)

LOG_LEVEL = "INFO"

logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "console": {
                "format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s",  # Format for console output
            },
            "file": {
                "format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"
            },  # Format for file output
            "django.server": DEFAULT_LOGGING["formatters"]["django.server"],
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",  # Outputs logs to the console
                "formatter": "console",  # Use the console formatter defined above
            },
            "file": {
                "level": "INFO",
                "class": "logging.FileHandler",  # Outputs logs to a file
                "formatter": "file",  # Use the file formatter defined above
                "filename": "logs/real_estate.log",  # File to which logs will be written
            },
            "django.server": DEFAULT_LOGGING["handlers"]["django.server"],
        },
        "loggers": {
            "": {
                "level": "INFO",  # Default level for all loggers
                "handlers": ["console", "file"],  # Use both console and file handlers
                "propagate": False,  # Do not send log messages to parent loggers
            },
            "apps": {
                "level": "INFO",  # Level for logs from the 'apps' namespace
                "handlers": ["console"],  # Only log to console for 'apps'
                "propagate": False,  # Do not send log messages to parent loggers
            },
            "django.server": DEFAULT_LOGGING["loggers"]["django.server"],
        },
    }
)
