"""
Django settings for app project.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/

Any setting that is configured via an environment variable may
also be set in a `.env` file in the project base directory.
"""
from os import path
from pathlib import Path

import django_heroku
import dj_database_url
from environs import Env
from furl import furl


# Build paths inside the project like this: path.join(BASE_PATH, ...)
BASE_PATH = Path(__file__).parent.parent
BASE_DIR = str(BASE_PATH)

env = Env()
env.read_env(str(BASE_PATH / ".env"), recurse=False)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY", "v8sk33sy82!uw3ty=!jjv5vp7=s2phrzw(m(hrn^f7e_#1h2al")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", True)

# True if you want to allow users to be able to create an account
ALLOW_SIGNUP = env.bool("ALLOW_SIGNUP", True)

# ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "server.apps.ServerConfig",
    "api.apps.ApiConfig",
    "widget_tweaks",
    "rest_framework",
    "django_filters",
    "polymorphic",
    "anymail",
    "piaf",
    "account",
]

CLOUD_BROWSER_APACHE_LIBCLOUD_PROVIDER = env("CLOUD_BROWSER_LIBCLOUD_PROVIDER", None)
CLOUD_BROWSER_APACHE_LIBCLOUD_ACCOUNT = env("CLOUD_BROWSER_LIBCLOUD_ACCOUNT", None)
CLOUD_BROWSER_APACHE_LIBCLOUD_SECRET_KEY = env("CLOUD_BROWSER_LIBCLOUD_KEY", None)

if CLOUD_BROWSER_APACHE_LIBCLOUD_PROVIDER:
    CLOUD_BROWSER_DATASTORE = "ApacheLibcloud"
    CLOUD_BROWSER_OBJECT_REDIRECT_URL = "/v1/cloud-upload"
    INSTALLED_APPS.append("cloud_browser")

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "applicationinsights.django.ApplicationInsightsMiddleware",
]

ROOT_URLCONF = "app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            str(BASE_PATH / "app" / "templates"),
            str(BASE_PATH / "authentification" / "templates"),
            str(BASE_PATH / "piaf" / "templates"),
            str(BASE_PATH / "piaf" / "static"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "libraries": {
                "analytics": "server.templatetags.analytics",
                "utils_templating": "authentification.templatetags.utils_templating",
            },
        },
    }
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = str(BASE_PATH / "staticfiles")

STATICFILES_DIRS = [
    static_path
    for static_path in (
        str(BASE_PATH / "server" / "static" / "assets"),
        str(BASE_PATH / "piaf" / "static" / "front"),
    )
    if path.isdir(static_path)
]


WSGI_APPLICATION = "app.wsgi.application"

AUTHENTICATION_BACKENDS = ["django.contrib.auth.backends.ModelBackend"]

SOCIAL_AUTH_GITHUB_KEY = env("OAUTH_GITHUB_KEY", None)
SOCIAL_AUTH_GITHUB_SECRET = env("OAUTH_GITHUB_SECRET", None)
GITHUB_ADMIN_ORG_NAME = env("GITHUB_ADMIN_ORG_NAME", None)
GITHUB_ADMIN_TEAM_NAME = env("GITHUB_ADMIN_TEAM_NAME", None)

if GITHUB_ADMIN_ORG_NAME and GITHUB_ADMIN_TEAM_NAME:
    SOCIAL_AUTH_GITHUB_SCOPE = ["read:org"]

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": str(BASE_PATH / "db.sqlite3"),
    }
}

AUTH_USER_MODEL = "account.User"

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly",
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 5,
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "SEARCH_PARAM": "q",
    "DEFAULT_RENDERER_CLASSES": (
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
        "rest_framework_xml.renderers.XMLRenderer",
    ),
}

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = "fr-fr"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEST_RUNNER = "xmlrunner.extra.djangotestrunner.XMLTestRunner"
TEST_OUTPUT_DIR = str(BASE_PATH / "junitxml")

LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/app/"
LOGOUT_REDIRECT_URL = "/"

django_heroku.settings(locals(), test_runner=False)

# Change 'default' database configuration with $DATABASE_URL.
DATABASES["default"].update(
    dj_database_url.config(
        env="DATABASE_URL",
        conn_max_age=env.int("DATABASE_CONN_MAX_AGE", 500),
        ssl_require="sslmode" not in furl(env("DATABASE_URL", "")).args,
    )
)

# work-around for dj-database-url: explicitly disable ssl for sqlite
if DATABASES["default"].get("ENGINE") == "django.db.backends.sqlite3":
    DATABASES["default"].get("OPTIONS", {}).pop("sslmode", None)

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Allow all host headers
# ALLOWED_HOSTS = ['*']

# Size of the batch for creating documents
# on the import phase
IMPORT_BATCH_SIZE = env.int("IMPORT_BATCH_SIZE", 500)

GOOGLE_TRACKING_ID = env("GOOGLE_TRACKING_ID", "")

## necessary for email verification setup
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'random@gmail.com'
# EMAIL_HOST_PASSWORD = 'gfds6jk#4ljIr%G8%'
# EMAIL_PORT = 587
#

MAILJET_API_KEY = env("MAILJET_API_KEY", None)
MAILJET_SECRET_KEY = env("MAILJET_SECRET_KEY", None)
USE_MAILJET = env.bool("USE_MAILJET", False)
DEFAULT_FROM_EMAIL = "piaf@data.gouv.fr"

WEBPACK_ENVIRONMENT_PRODUCTION = env.bool("WEBPACK_ENVIRONMENT_PRODUCTION", True)
MATOMO_SITE_ID = env("MATOMO_SITE_ID", "")

# information here: https://anymail.readthedocs.io/en/stable/esps/mailjet/
ANYMAIL = {"MAILJET_API_KEY": MAILJET_API_KEY, "MAILJET_SECRET_KEY": MAILJET_SECRET_KEY}

if USE_MAILJET:
    EMAIL_BACKEND = "anymail.backends.mailjet.EmailBackend"
else:
    ## During development only
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": str(BASE_PATH / "debug.log"),
        }
    },
    "loggers": {"django": {"handlers": ["file"], "level": "ERROR", "propagate": True}},
}
