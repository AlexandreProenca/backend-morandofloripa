# coding: utf-8
from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
import views

router = routers.DefaultRouter()
router.register(r'users', views.UserView, 'list')
router.register(r'gostos', views.GostoView, 'list')
router.register(r'perfils', views.PerfilView, 'list')
router.register(r'intencaos', views.IntencaoView, 'list')
router.register(r'beneficios', views.BeneficioView, 'list')
router.register(r'regras', views.RegraView, 'list')
router.register(r'iteminclusos', views.ItemInclusoView, 'list')
router.register(r'periodos', views.PeriodoView, 'list')
router.register(r'tipoimovels', views.TipoImovelView, 'list')
router.register(r'imovels', views.ImovelView, 'list')
router.register(r'imovelhasvisitas', views.ImovelHasVisitaView, 'list')
router.register(r'valors', views.ValorView, 'list')
router.register(r'anuncios', views.AnuncioView, 'list')
router.register(r'anunciohasinteressados', views.AnuncioHasInteressadoView, 'list')
router.register(r'disponibilidades', views.DisponibilidadeView, 'list')
router.register(r'enderecos', views.EnderecoView, 'list')
router.register(r'telefones', views.TelefoneView, 'list')
router.register(r'perfilhasgostoss', views.PerfilHasGostosView, 'list')
router.register(r'imovelhasavaliacaos', views.ImovelHasAvaliacaoView, 'list')
router.register(r'lugarproximos', views.LugarProximoView, 'list')
router.register(r'mensagems', views.MensagemView, 'list')
router.register(r'midias', views.MidiaView, 'list')
router.register(r'imovelhaslugarproximos', views.ImovelHasLugarProximoView, 'list')
router.register(r'imovelhasbeneficios', views.ImovelHasBeneficioView, 'list')
router.register(r'imovelhasregras', views.ImovelHasRegraView, 'list')
router.register(r'imovelhasiteminclusos', views.ImovelHasItemInclusoView, 'list')
router.register(r'imovelhasperiodos', views.ImovelHasPeriodoView, 'list')
router.register(r'imovelhasvalors', views.ImovelHasValorView, 'list')
router.register(r'imovelhasdisponibilidades', views.ImovelHasDisponibilidadeView, 'list')
router.register(r'imovelindicadogostos', views.ImovelIndicadoGostoView, 'list')

urlpatterns = patterns('',)

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += patterns('', url(r'^', include(router.urls)),)
