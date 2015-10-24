# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver


class Avaliacao(models.Model):
    de = models.ForeignKey(User)
    estrelas = models.IntegerField(blank=True, null=True)
    mensagem = models.TextField(blank=True, null=True)
    imovel = models.ForeignKey('Imovel')
    like = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'avaliacao'

    def __unicode__(self):
        return


class Imovel(models.Model):
    tipo = models.CharField(max_length=9, blank=True, null=True)
    whatsapp_contato = models.CharField(max_length=45, blank=True, null=True)
    telefone_contato = models.CharField(max_length=45, blank=True, null=True)
    email_contato = models.CharField(max_length=255, blank=True, null=True)
    metro_quadrado = models.FloatField(blank=True, null=True)
    valor_diaria = models.FloatField(blank=True, null=True)
    valor_mensal = models.FloatField(blank=True, null=True)
    periodo_anual = models.DateField(blank=True, null=True)
    periodo_temporada = models.DateField(blank=True, null=True)
    qt_quartos = models.IntegerField(blank=True, null=True)
    qt_garagem = models.IntegerField(blank=True, null=True)
    qt_moradores = models.IntegerField(blank=True, null=True)
    aceita_animais = models.BooleanField(default=False)
    aceita_sexo = models.CharField(max_length=9, blank=True, null=True)
    aceita_criancas = models.BooleanField(default=False)
    aceita_tabaco = models.BooleanField(default=False)
    aceita_tocar_instrumento = models.BooleanField(default=False)
    aceita_visita_de_amigos = models.BooleanField(default=False)
    aceita_festas = models.BooleanField(default=False)
    alugado = models.BooleanField(default=False)
    unica_terreno = models.BooleanField(default=False)
    mobilhado = models.CharField(max_length=4, blank=True, null=True)
    possue_vigilacia = models.BooleanField(default=False)
    possue_ar_condicionado = models.BooleanField(default=False)
    possue_sacada = models.BooleanField(default=False)
    possue_maq_lavar = models.BooleanField(default=False)
    possue_fogao = models.BooleanField(default=False)
    possue_geladeira = models.BooleanField(default=False)
    possue_microondas = models.BooleanField(default=False)
    possue_churrasqueira = models.BooleanField(default=False)
    possue_banheiro_externo = models.BooleanField(default=False)
    possue_cama = models.BooleanField(default=False)
    possue_liquidificador = models.BooleanField(default=False)
    possue_grill = models.BooleanField(default=False)
    possue_torradeira = models.BooleanField(default=False)
    possue_mesa = models.BooleanField(default=False)
    possue_orta = models.BooleanField(default=False)
    possue_piscina = models.BooleanField(default=False)
    possue_tv_cabo = models.BooleanField(default=False)
    possue_garagem = models.BooleanField(default=False)
    possue_tv = models.BooleanField(default=False)
    incluso_internet = models.BooleanField(default=False)
    incluso_luz = models.BooleanField(default=False)
    incluso_agua = models.BooleanField(default=False)
    incluso_tv_cabo = models.BooleanField(default=False)
    disponivel_a_partir_de = models.DateField(blank=True, null=True)
    disponivel_ate = models.DateField(blank=True, null=True)
    horario_visita_inicio = models.TimeField(blank=True, null=True)
    horario_visita_fim = models.TimeField(blank=True, null=True)
    bairro = models.CharField(max_length=45, blank=True, null=True)
    nome_rua = models.CharField(max_length=100, blank=True, null=True)
    numero_casa_ap = models.IntegerField(blank=True, null=True)
    cep_imovel = models.CharField(max_length=45, blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)
    cidade = models.CharField(max_length=45, blank=True, null=True)
    valor_medio_agua_por_morador = models.FloatField(blank=True, null=True)
    valor_medio_luz_por_morador = models.FloatField(blank=True, null=True)
    valor_medio_internet_por_morador = models.FloatField(blank=True, null=True)
    valor_medio_aluguel_por_morador = models.FloatField(blank=True, null=True)
    valor_max_aluguel_morador = models.FloatField(blank=True, null=True)
    alugo_ou_procuro = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    proprietario = models.ForeignKey(User)

    class Meta:
        managed = True
        db_table = 'imovel'


class LugarProximo(models.Model):
    nome = models.CharField(max_length=45, blank=True, null=True)
    tipo = models.CharField(max_length=12, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    imovel = models.ForeignKey(Imovel)

    class Meta:
        managed = True
        db_table = 'lugar_proximo'


class Mensagem(models.Model):
    de = models.ForeignKey(User)
    titulo = models.CharField(max_length=100, blank=True, null=True)
    mensagem = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    imovel = models.ForeignKey(Imovel)

    class Meta:
        managed = True
        db_table = 'mensagem'


class Midia(models.Model):
    link = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.CharField(max_length=6, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    imovel = models.ForeignKey(Imovel)

    class Meta:
        managed = True
        db_table = 'midia'


class Perfil(models.Model):
    user = models.ForeignKey(User)
    curte_skate = models.BooleanField(default=False)
    curte_long_bord = models.BooleanField(default=False)
    curte_surf = models.BooleanField(default=False)
    curte_kite = models.BooleanField(default=False)
    curte_sup = models.BooleanField(default=False)
    curte_praia = models.BooleanField(default=False)
    curte_balada = models.BooleanField(default=False)
    curte_sussego = models.BooleanField(default=False)
    curte_natureza = models.BooleanField(default=False)
    curte_escalada = models.BooleanField(default=False)
    estuda_na_ufsc = models.BooleanField(default=False)
    estuda_na_udesc = models.BooleanField(default=False)
    curte_slackline = models.BooleanField(default=False)
    curte_mergulho = models.BooleanField(default=False)
    curte_montanha = models.BooleanField(default=False)
    curte_nadar = models.BooleanField(default=False)
    curte_bike = models.BooleanField(default=False)
    curte_organicos = models.BooleanField(default=False)
    curte_cerveja_caseira = models.BooleanField(default=False)
    curte_paraquedismo = models.BooleanField(default=False)
    curte_parapente = models.BooleanField(default=False)
    curte_kayake = models.BooleanField(default=False)
    curte_animais = models.BooleanField(default=False)
    data_nascimento = models.DateField(blank=True, null=True)
    direcao_trabalho = models.CharField(max_length=6, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'perfil'


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

#-----------------------------------------------------#
#--------SUPER HACK - DONT TOUCH THIS NEVER-----------#
#-----------------------------------------------------#
def hack_models(length=100):
    from django.contrib.auth.models import User
    username = User._meta.get_field("username")
    username.max_length = length
    hack_validators(username.validators)


def hack_validators(validators, length=100):
    from django.core.validators import MaxLengthValidator
    for key, validator in enumerate(validators):
        if isinstance(validator, MaxLengthValidator):
            validators.pop(key)
    validators.insert(0, MaxLengthValidator(length))

#Seta o max_lenght do username para 100
hack_models(length=100)
#-----------------------------------------------------#