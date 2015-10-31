# coding: utf-8
from django.contrib import admin
import models


class TipoGosto(admin.ModelAdmin):
    list_display = ['id', 'nome', 'tipo']

class Perfil(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'CPF', 'imagem', 'whatsapp', 'facebook', 'data_nascimento', 'sexo', 'nacionalidade', 'alugo_procuro']

class TipoIntencao(admin.ModelAdmin):
    list_display = ['id', 'nome', 'tipo']

class TipoBeneficio(admin.ModelAdmin):
    list_display = ['id', 'nome', 'tipo']

class TipoRegra(admin.ModelAdmin):
    list_display = ['id', 'nome', 'tipo']

class TipoItemIncluso(admin.ModelAdmin):
    list_display = ['id', 'nome', 'tipo']

class TipoPeriodo(admin.ModelAdmin):
    list_display = ['id', 'nome', 'tipo']

class TipoImovel(admin.ModelAdmin):
    list_display = ['id', 'nome', 'tipo']

class Imovel(admin.ModelAdmin):
    list_display = ['id', 'metro_quadrado', 'bairro', 'nome_rua', 'numero_casa_ap', 'cep_imovel', 'observacoes', 'cidade', 'venda', 'disponivel', 'created', 'proprietario', 'tipo_imovel']

class ImovelHasVisita(admin.ModelAdmin):
    list_display = ['id', 'imovel', 'visitante', 'data', 'observacoes', 'created']

class TipoValor(admin.ModelAdmin):
    list_display = ['id', 'nome', 'tipo']

class Anuncio(admin.ModelAdmin):
    list_display = ['id', 'data_inicio', 'data_final', 'created', 'imovel']

class AnuncioHasInteressado(admin.ModelAdmin):
    list_display = ['id', 'anuncio', 'interessado', 'created']

class TipoData(admin.ModelAdmin):
    list_display = ['id', 'nome', 'tipo']

class Endereco(admin.ModelAdmin):
    list_display = ['id', 'cidade', 'bairro', 'rua', 'complemento', 'cep', 'tipo', 'perfil']

class Telefone(admin.ModelAdmin):
    list_display = ['id', 'numero', 'ddd', 'tipo', 'operadora', 'perfil']

class PerfilHasGostos(admin.ModelAdmin):
    list_display = ['id', 'perfil', 'gosto']

class ImovelHasAvaliacao(admin.ModelAdmin):
    list_display = ['id', 'imovel', 'avaliador', 'estrelas', 'mensagem', 'created']

class TipoLugarProximo(admin.ModelAdmin):
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
    list_display = ['id', 'imovel', 'valor', 'preco']

class ImovelHasDisponibilidade(admin.ModelAdmin):
    list_display = ['id', 'imovel', 'data', 'disponibilidade']

class ImovelIndicadoGosto(admin.ModelAdmin):
    list_display = ['id', 'imovel', 'gosto']

class ImovelIndicadoIntencao(admin.ModelAdmin):
    list_display = ['id', 'imovel', 'intencao']


admin.site.register(models.TipoGosto, TipoGosto)
admin.site.register(models.Perfil, Perfil)
admin.site.register(models.TipoIntencao, TipoIntencao)
admin.site.register(models.TipoBeneficio, TipoBeneficio)
admin.site.register(models.TipoRegra, TipoRegra)
admin.site.register(models.TipoItemIncluso, TipoItemIncluso)
admin.site.register(models.TipoPeriodo, TipoPeriodo)
admin.site.register(models.TipoImovel, TipoImovel)
admin.site.register(models.Imovel, Imovel)
admin.site.register(models.ImovelHasVisita, ImovelHasVisita)
admin.site.register(models.TipoValor, TipoValor)
admin.site.register(models.Anuncio, Anuncio)
admin.site.register(models.AnuncioHasInteressado, AnuncioHasInteressado)
admin.site.register(models.TipoData, TipoData)
admin.site.register(models.Endereco, Endereco)
admin.site.register(models.Telefone, Telefone)
admin.site.register(models.PerfilHasGostos, PerfilHasGostos)
admin.site.register(models.ImovelHasAvaliacao, ImovelHasAvaliacao)
admin.site.register(models.TipoLugarProximo, TipoLugarProximo)
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
admin.site.register(models.ImovelIndicadoIntencao, ImovelIndicadoIntencao)
