# coding: utf-8
from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
import views

router = routers.DefaultRouter()
router.register(r'users', views.UserView, 'list')
router.register(r'avaliacoes', views.AvaliacaoView, 'list')
router.register(r'imoveis', views.ImovelView, 'list')
router.register(r'lugarproximos', views.LugarProximoView, 'list')
router.register(r'mensagems', views.MensagemView, 'list')
router.register(r'midias', views.MidiaView, 'list')
router.register(r'perfils', views.PerfilView, 'list')

urlpatterns = patterns('',)

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += patterns('', url(r'^', include(router.urls)),)
