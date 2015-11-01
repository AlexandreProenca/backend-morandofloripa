"""liberdade URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^v1/docs/', include('rest_framework_swagger.urls')),
    url(r'^v1/auth/', include('rest_framework_social_oauth2.urls')),
    url(r'^v1/token-auth/', 'core.views.obtain_auth_token'),
    url(r'^v1/password-reset/$', 'core.views.password_reset', {'post_reset_redirect' : '/accounts/password_reset/mailed/'}, name='password-reset'),
    #to use management credentials in web page and reset password
    url(r'^v1/accounts/password_reset/$', 'django.contrib.auth.views.password_reset', {'post_reset_redirect': '/accounts/password_reset/mailed/'}, name="password_reset"),
    url(r'^v1/accounts/password_reset/mailed/$','django.contrib.auth.views.password_reset_done', name="password_reset_confirm"),
    url(r'^v1/accounts/password_reset/(?P<uidb64>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 'django.contrib.auth.views.password_reset_confirm',  {'post_reset_redirect' : '/accounts/password_reset/complete/'}, name="password_reset_confirm"),
    url(r'^v1/accounts/password_reset/complete/$','django.contrib.auth.views.password_reset_complete'),
    url(r'^v1/o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^v1/rest-auth/', include('rest_auth.urls')),
    #url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^v1/', include('core.urls')),
]
