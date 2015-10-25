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
        'NAME': 'nwpartner9',
        'USER': 'nwpartner9',
        'PASSWORD': 'gmmaster765',
        'HOST': '187.45.196.238',
        'PORT': '3306',
    }
}

#Django Restframework configuration
REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': (
        #'oauth2_provider.ext.rest_framework.OAuth2Authentication',
        #'rest_framework.authentication.BasicAuthentication',
        #'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),

    'DEFAULT_PERMISSION_CLASSES':(
        'rest_framework.permissions.AllowAny',
        #'rest_framework.permissions.IsAuthenticated',
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
