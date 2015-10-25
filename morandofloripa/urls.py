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
    url(r'^docs/', include('rest_framework_swagger.urls')),
    #url(r'^oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    #url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include('core.urls')),
]
