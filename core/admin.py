# coding: utf-8
from django.contrib import admin
import models


class Avaliacao(admin.ModelAdmin):
    list_display = ['id', 'de', 'estrelas', 'mensagem', 'imovel', 'like']

class Imovel(admin.ModelAdmin):
    list_display = ['id', 'tipo', 'whatsapp_contato', 'telefone_contato', 'email_contato', 'metro_quadrado', 'valor_diaria', 'valor_mensal', 'periodo_anual', 'periodo_temporada', 'qt_quartos', 'qt_garagem', 'qt_moradores', 'aceita_animais', 'aceita_sexo', 'aceita_criancas', 'aceita_tabaco', 'aceita_tocar_instrumento', 'aceita_visita_de_amigos', 'aceita_festas', 'alugado', 'unica_terreno', 'mobilhado', 'possue_vigilacia', 'possue_ar_condicionado', 'possue_sacada', 'possue_maq_lavar', 'possue_fogao', 'possue_geladeira', 'possue_microondas', 'possue_churrasqueira', 'possue_banheiro_externo', 'possue_cama', 'possue_liquidificador', 'possue_grill', 'possue_torradeira', 'possue_mesa', 'possue_orta', 'possue_piscina', 'possue_tv_cabo', 'possue_garagem', 'possue_tv', 'incluso_internet', 'incluso_luz', 'incluso_agua', 'incluso_tv_cabo', 'disponivel_a_partir_de', 'disponivel_ate', 'horario_visita_inicio', 'horario_visita_fim', 'bairro', 'nome_rua', 'numero_casa_ap', 'cep_imovel', 'observacoes', 'cidade', 'valor_medio_agua_por_morador', 'valor_medio_luz_por_morador', 'valor_medio_internet_por_morador', 'valor_medio_aluguel_por_morador', 'valor_max_aluguel_morador', 'alugo_ou_procuro', 'created', 'proprietario']

class LugarProximo(admin.ModelAdmin):
    list_display = ['id', 'nome', 'tipo', 'created', 'imovel']

class Mensagem(admin.ModelAdmin):
    list_display = ['id', 'de', 'titulo', 'mensagem', 'created', 'imovel']

class Midia(admin.ModelAdmin):
    list_display = ['id', 'link', 'tipo', 'created', 'imovel']

class Perfil(admin.ModelAdmin):
    list_display = ['id', 'user', 'curte_skate', 'curte_long_bord', 'curte_surf', 'curte_kite', 'curte_sup', 'curte_praia', 'curte_balada', 'curte_sussego', 'curte_natureza', 'curte_escalada', 'estuda_na_ufsc', 'estuda_na_udesc', 'curte_slackline', 'curte_mergulho', 'curte_montanha', 'curte_nadar', 'curte_bike', 'curte_organicos', 'curte_cerveja_caseira', 'curte_paraquedismo', 'curte_parapente', 'curte_kayake', 'curte_animais', 'data_nascimento', 'direcao_trabalho', 'created']


admin.site.register(models.Avaliacao, Avaliacao)
admin.site.register(models.Imovel, Imovel)
admin.site.register(models.LugarProximo, LugarProximo)
admin.site.register(models.Mensagem, Mensagem)
admin.site.register(models.Midia, Midia)
admin.site.register(models.Perfil, Perfil)
