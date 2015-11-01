from defaults import *

DEBUG = True

# DATABASES = {
#      'default': {
#          'ENGINE': 'django.db.backends.sqlite3',
#          'NAME': 'base_teste',
#      }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get("MYAPP_DB_USER", ''),
        'USER': os.environ.get("MYAPP_DB_USER", ''),
        'PASSWORD': os.environ.get("MYAPP_DB_PASSWORD", ''),
        'HOST': os.environ.get("HOST_DB_MF", ''),
        'PORT': '3306',
    }
}

#Django Restframework configuration
REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',
        'rest_framework_social_oauth2.authentication.SocialAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),

    'DEFAULT_PERMISSION_CLASSES':(
        'rest_framework.permissions.IsAuthenticated',
    ),

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SWAGGER_SETTINGS = {
    'exclude_namespaces': [],
    'api_version': '',
    'api_path': '/',
    'enabled_methods': [
        'get',
        'post',
        'put',
        'patch',
        'delete'
    ],
    'api_key': '',
    'is_authenticated': False,
    'is_superuser': False,
    'permission_denied_handler': None,
    'info': {
        'contact': '',
        'description': '',
        'title': '',
    },
    'doc_expansion': 'none',
}
