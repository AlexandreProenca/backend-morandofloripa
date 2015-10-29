# coding: utf-8
from django.contrib import admin
import models


class Gosto(admin.ModelAdmin):
    list_display = ['id', 'nome']

class Perfil(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'CPF', 'whatsapp', 'facebook', 'data_nascimento', 'sexo', 'nacionalidade', 'alugo_procuro']

class Intencao(admin.ModelAdmin):
    list_display = ['id', 'nome', 'tipo']

class Beneficio(admin.ModelAdmin):

    list_display = ['id', 'nome', 'tipo']

class Regra(admin.ModelAdmin):
    list_display = ['id', 'nome', 'tipo']

class ItemIncluso(admin.ModelAdmin):
    list_display = ['id', 'nome', 'tipo']

class Periodo(admin.ModelAdmin):
    list_display = ['id', 'nome', 'tipo']

class TipoImovel(admin.ModelAdmin):
    list_display = ['id', 'nome', 'tipo']

class Imovel(admin.ModelAdmin):
    list_display = ['id', 'metro_quadrado', 'bairro', 'nome_rua', 'numero_casa_ap', 'cep_imovel', 'observacoes', 'cidade', 'venda', 'disponivel', 'created', 'proprietario', 'tipo_imovel']

class ImovelHasVisita(admin.ModelAdmin):
    list_display = ['id', 'imovel', 'visitante', 'data', 'observacoes', 'created']

class Valor(admin.ModelAdmin):
    list_display = ['id', 'nome', 'tipo']

class Anuncio(admin.ModelAdmin):
    list_display = ['id', 'data_inicio', 'data_final', 'created', 'imovel']

class AnuncioHasInteressado(admin.ModelAdmin):
    list_display = ['id', 'anuncio', 'interessado', 'created']

class Disponibilidade(admin.ModelAdmin):
    list_display = ['id', 'data_inicio', 'data_final']

class Endereco(admin.ModelAdmin):
    list_display = ['id', 'cidade', 'bairro', 'rua', 'complemento', 'cep', 'tipo', 'perfil']

class Telefone(admin.ModelAdmin):
    list_display = ['id', 'numero', 'ddd', 'tipo', 'operadora', 'perfil']

class PerfilHasGostos(admin.ModelAdmin):
    list_display = ['id', 'perfil', 'gosto']

class ImovelHasAvaliacao(admin.ModelAdmin):
    list_display = ['id', 'imovel', 'avaliador', 'estrelas', 'mensagem', 'created']

class LugarProximo(admin.ModelAdmin):
    list_display = ['id', 'nome', 'tipo']

class Mensagem(admin.ModelAdmin):
    list_display = ['id', 'de', 'para', 'titulo', 'mensagem', 'enviada', 'visualizada', 'created']

class Midia(admin.ModelAdmin):
    list_display = ['id', 'link', 'tipo', 'imovel']

class ImovelHasLugarProximo(admin.ModelAdmin):
    list_display = ['id', 'imovel', 'lugar_proximo']

class ImovelHasBeneficio(admin.ModelAdmin):
    list_display = ['id', 'imovel', 'beneficio', 'metro_quadrado', 'quantidade']

class ImovelHasRegra(admin.ModelAdmin):
    list_display = ['id', 'imovel', 'regra', 'possibilidade']

class ImovelHasItemIncluso(admin.ModelAdmin):
    list_display = ['id', 'imovel', 'item']

class ImovelHasPeriodo(admin.ModelAdmin):
    list_display = ['id', 'imovel', 'periodo']

class ImovelHasValor(admin.ModelAdmin):
    list_display = ['id', 'imovel', 'valor']

class ImovelHasDisponibilidade(admin.ModelAdmin):
    list_display = ['id', 'imovel', 'disponibilidade']

class ImovelIndicadoGosto(admin.ModelAdmin):
    list_display = ['id', 'imovel', 'gosto']


admin.site.register(models.Gosto, Gosto)
admin.site.register(models.Perfil, Perfil)
admin.site.register(models.Intencao, Intencao)
admin.site.register(models.Beneficio, Beneficio)
admin.site.register(models.Regra, Regra)
admin.site.register(models.ItemIncluso, ItemIncluso)
admin.site.register(models.Periodo, Periodo)
admin.site.register(models.TipoImovel, TipoImovel)
admin.site.register(models.Imovel, Imovel)
admin.site.register(models.ImovelHasVisita, ImovelHasVisita)
admin.site.register(models.Valor, Valor)
admin.site.register(models.Anuncio, Anuncio)
admin.site.register(models.AnuncioHasInteressado, AnuncioHasInteressado)
admin.site.register(models.Disponibilidade, Disponibilidade)
admin.site.register(models.Endereco, Endereco)
admin.site.register(models.Telefone, Telefone)
admin.site.register(models.PerfilHasGostos, PerfilHasGostos)
admin.site.register(models.ImovelHasAvaliacao, ImovelHasAvaliacao)
admin.site.register(models.LugarProximo, LugarProximo)
admin.site.register(models.Mensagem, Mensagem)
admin.site.register(models.Midia, Midia)
admin.site.register(models.ImovelHasLugarProximo, ImovelHasLugarProximo)
admin.site.register(models.ImovelHasBeneficio, ImovelHasBeneficio)
admin.site.register(models.ImovelHasRegra, ImovelHasRegra)
admin.site.register(models.ImovelHasItemIncluso, ImovelHasItemIncluso)
admin.site.register(models.ImovelHasPeriodo, ImovelHasPeriodo)
admin.site.register(models.ImovelHasValor, ImovelHasValor)
admin.site.register(models.ImovelHasDisponibilidade, ImovelHasDisponibilidade)
admin.site.register(models.ImovelIndicadoGosto, ImovelIndicadoGosto)
