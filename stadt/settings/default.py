"""
Django settings for stadtgestalten project.
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = BASE_DIR if os.access(BASE_DIR, os.W_OK) else os.path.expanduser("~")

# Application definition
INSTALLED_APPS = [
    'account.apps.AccountConfig',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'content',
    'core.apps.CoreConfig',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.forms',
    'django_filters',
    'django_mailbox',
    'entities.apps.EntitiesConfig',
    'features.articles',
    'features.associations',
    'features.contributions',
    'features.conversations',
    'features.caching',
    'features.content',
    'features.events',
    'features.galleries',
    'features.gestalten',
    'features.groups',
    'features.images',
    'features.memberships.apps.MembershipsConfig',
    'features.sharing',
    'features.stadt',
    'features.subscriptions',
    'features.tags',
    'features.texts',
    'rest_framework',
    'rules.apps.AutodiscoverRulesConfig',
    'sorl.thumbnail',
    'utils',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'features.gestalten.middleware.GestaltAppConfigMiddleware',
    'stadt.middleware.DoesNotExistMiddleware',
]

ROOT_URLCONF = 'stadt.urls'

TEMPLATES = [
    {
        'APP_DIRS': True,
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'stadt', 'templates'),
        ],
        'OPTIONS': {
            'builtins': ['core.templatetags.core'],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'features.caching.context_processors.cache_timeout',
                'features.groups.context_processors.groups',
                'features.memberships.context_processors.my_memberships',
                'features.stadt.context_processors.page_meta',
                'stadt.context_processors.site',
                'stadt.context_processors.assets',
            ],
        },
    },
]

FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'


WSGI_APPLICATION = 'stadt.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DATA_DIR, 'db.sqlite3')
    }
}


# Authentication backends
# https://docs.djangoproject.com/en/1.9/topics/auth/customizing/#authentication-backends

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    'rules.permissions.ObjectPermissionBackend',
]


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
            'django.contrib.auth.password_validation'
            '.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation'
            '.MinimumLengthValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation'
            '.CommonPasswordValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation'
            '.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'de-de'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    ('stadt', os.path.join(BASE_DIR, 'build', 'static')),
]


# User uploaded files
# https://docs.djangoproject.com/en/1.9/topics/files/

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')


# Email
# https://docs.djangoproject.com/en/1.9/topics/email/

ACCOUNT_EMAIL_SUBJECT_PREFIX = ''

DEFAULT_FROM_EMAIL = 'noreply@localhost'
DEFAULT_REPLY_TO_EMAIL = 'stadtgestalten+{reply_key}@localhost'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Sites
# https://docs.djangoproject.com/en/1.9/ref/contrib/sites/

SITE_ID = 1


# Stadtgestalten
#

ABOUT_GROUP_ID = 1

SCORE_CONTENT_AGE = 100

SCORE_PROCESSORS = [
    'features.stadt.scores.Gestalt',
    'features.stadt.scores.Group',
]

ROOT_SIGNALCONF = 'stadt.signals'

BACKUP_PATH = '/var/backups/stadtgestalten'


# Authentication
# http://django-allauth.readthedocs.org/

LOGIN_URL = 'account_login'

LOGIN_REDIRECT_URL = 'index'

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'

ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'http'

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_LOGIN_ON_PASSWORD_RESET = True

ACCOUNT_USER_DISPLAY = lambda u: u.gestalt    # noqa: E731

ACCOUNT_USERNAME_REQUIRED = False


# Crispy forms
# http://django-crispy-forms.readthedocs.org/

CRISPY_TEMPLATE_PACK = 'bootstrap3'


# Caching
# https://docs.djangoproject.com/en/1.10/topics/cache/

CACHES = {
    'default': {
        'BACKEND': 'features.caching.backends.ProxyCache',
    },
    'proxy': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    },
    'test': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
}


# Django Rest Framework
# http://www.django-rest-framework.org/

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'core.permissions.RulesPermissions',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
    ),
}

INTERNAL_IPS = ("127.0.0.1", )

# string       : entity      : the entity as model string that is being watched
# list[string] : props       : the props that are checked for tags
# boolean      : tag_self    : if the entity itself should be tagged, when one of the props passed
# list[lambda] : tag_related : list of related objects (via lambda) that should be tagged
# lambda       : constraint  : return false to skip
#
# only entity and props are required
TAGS_TAGGABLE = (
    {'entity': 'content.Comment', 'props': ['text'], 'tag_related': [
        lambda comment: comment.content
    ]},
    {'entity': 'content.Content', 'props': ['text', 'title']},
    # FIXME make this work for contributions
    # {'entity': 'texts.Text', 'props': ['text'],
    #  'constraint': lambda text: text.conversation is not None, 'tag_related': [
    #     lambda text: text.conversation
    # ]}
)

try:
    ASSET_VERSION = open(os.path.join(BASE_DIR, "stadt", "ASSET_VERSION"), "r").read().strip()
except IOError:
    ASSET_VERSION = "trunk"

try:
    CACHE_VERSION = int(open(os.path.join(BASE_DIR, "stadt", "CACHE_VERSION"), "r").read().strip())
except IOError:
    CACHE_VERSION = 1
