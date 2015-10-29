# coding: utf-8
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



class Gosto(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'gosto'

    def __unicode__(self):
        return self.nome


class Perfil(models.Model):
    usuario = models.ForeignKey(User)
    CPF = models.CharField(max_length=11, blank=True, null=True)
    whatsapp = models.CharField(max_length=15, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    nacionalidade = models.CharField(max_length=50, blank=True, null=True)
    alugo_procuro = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'perfil'

    def __unicode__(self):
        return self.usuario.first_name


class Intencao(models.Model):

    nome = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'intencao'

    def __unicode__(self):
        return self.nome


class Beneficio(models.Model):

    nome = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'beneficio'

    def __unicode__(self):
        return self.nome


class Regra(models.Model):

    nome = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'regra'

    def __unicode__(self):
        return self.nome


class ItemIncluso(models.Model):

    nome = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'item_incluso'

    def __unicode__(self):
        return self.nome

class Periodo(models.Model):

    nome = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'periodo'

    def __unicode__(self):
        return self.nome

class TipoImovel(models.Model):

    nome = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tipo_imovel'

    def __unicode__(self):
        return self.nome


class Imovel(models.Model):
    metro_quadrado = models.FloatField(blank=True, null=True)
    bairro = models.CharField(max_length=45, blank=True, null=True)
    nome_rua = models.CharField(max_length=100, blank=True, null=True)
    numero_casa_ap = models.IntegerField(blank=True, null=True)
    cep_imovel = models.CharField(max_length=45, blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)
    cidade = models.CharField(max_length=45, blank=True, null=True)
    venda = models.BooleanField(default=False)
    disponivel = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    proprietario = models.ForeignKey(User)
    tipo_imovel = models.ForeignKey(TipoImovel)

    class Meta:
        managed = True
        db_table = 'imovel'

    def __unicode__(self):

        return "Imovel"

class ImovelHasVisita(models.Model):
    imovel = models.ForeignKey(Imovel)
    visitante = models.ForeignKey(User)
    data = models.DateTimeField()
    observacoes = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'imovel_has_visita'


class Valor(models.Model):
    nome = models.CharField(max_length=45, blank=True, null=True)
    tipo = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'valor'

    def __unicode__(self):
        return self.nome

class Anuncio(models.Model):
    data_inicio = models.DateTimeField()
    data_final = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    imovel = models.ForeignKey(Imovel)

    class Meta:
        managed = True
        db_table = 'anuncio'

    def __unicode__(self):
        return self.imovel_id


class AnuncioHasInteressado(models.Model):
    anuncio = models.ForeignKey(Anuncio)
    interessado = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'anuncio_has_interessado'



class Disponibilidade(models.Model):
    data_inicio = models.DateField()
    data_final = models.DateField()

    class Meta:
        managed = True
        db_table = 'disponibilidade'

    def __unicode__(self):
        return str(self.data_inicio)


class Endereco(models.Model):
    cidade = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    rua = models.CharField(max_length=100, blank=True, null=True)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=100, blank=True, null=True)
    perfil = models.ForeignKey(Perfil)

    class Meta:
        managed = True
        db_table = 'endereco'


class Telefone(models.Model):
    numero = models.IntegerField(blank=True, null=True)
    ddd = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    operadora = models.CharField(max_length=50, blank=True, null=True)
    perfil = models.ForeignKey(Perfil)

    class Meta:
        managed = True
        db_table = 'telefone'

class PerfilHasGostos(models.Model):
    perfil = models.ForeignKey(Perfil)
    gosto = models.ForeignKey(Gosto)

    class Meta:
        managed = True
        db_table = 'perfil_has_gostos'


class ImovelHasAvaliacao(models.Model):
    imovel = models.ForeignKey(Imovel)
    avaliador = models.ForeignKey(User)
    estrelas = models.IntegerField()
    mensagem = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'imovel_has_avaliacao'


class LugarProximo(models.Model):
    nome = models.CharField(max_length=45, blank=True, null=True)
    tipo = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lugar_proximo'

    def __unicode__(self):
        return self.nome

class Mensagem(models.Model):
    de = models.ForeignKey(User, related_name='de')
    para = models.ForeignKey(User, related_name='para')
    titulo = models.CharField(max_length=45, blank=True, null=True)
    mensagem = models.TextField(max_length=45, blank=True, null=True)
    enviada = models.DateTimeField(blank=True, null=True)
    visualizada = models.DateTimeField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'mensagem'


class Midia(models.Model):
    link = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.CharField(max_length=6, blank=True, null=True)
    imovel = models.ForeignKey(Imovel)

    class Meta:
        managed = True
        db_table = 'midia'

class ImovelHasLugarProximo(models.Model):
    imovel = models.ForeignKey(Imovel)
    lugar_proximo = models.ForeignKey(LugarProximo)

    class Meta:
        managed = True
        db_table = 'imovel_has_lugar_proximo'

class ImovelHasBeneficio(models.Model):
    imovel = models.ForeignKey(Imovel)
    beneficio = models.ForeignKey(Beneficio)
    metro_quadrado = models.FloatField(blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'imovel_has_beneficio'

class ImovelHasRegra(models.Model):
    imovel = models.ForeignKey(Imovel)
    regra = models.ForeignKey(Regra)
    possibilidade = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'imovel_has_regra'

class ImovelHasItemIncluso(models.Model):
    imovel = models.ForeignKey(Imovel)
    item = models.ForeignKey(ItemIncluso)

    class Meta:
        managed = True
        db_table = 'imovel_has_item_incluso'


class ImovelHasPeriodo(models.Model):
    imovel = models.ForeignKey(Imovel)
    periodo = models.ForeignKey(Periodo)

    class Meta:
        managed = True
        db_table = 'imovel_has_periodo'


class ImovelHasValor(models.Model):
    imovel = models.ForeignKey(Imovel)
    valor = models.ForeignKey(Valor)
    preco = models.CharField(max_length='20')

    class Meta:
        managed = True
        db_table = 'imovel_has_valor'


class ImovelHasDisponibilidade(models.Model):
    imovel = models.ForeignKey(Imovel)
    disponibilidade = models.ForeignKey(Disponibilidade)

    class Meta:
        managed = True
        db_table = 'imovel_has_disponibilidade'


class ImovelIndicadoGosto(models.Model):
    imovel = models.ForeignKey(Imovel)
    gosto = models.ForeignKey(Gosto)

    class Meta:
        managed = True
        db_table = 'imovel_indicado_gosto'


class ImovelIndicadoIntencao(models.Model):
    imovel = models.ForeignKey(Imovel)
    intencao = models.ForeignKey(Intencao)

    class Meta:
        managed = True
        db_table = 'imovel_indicado_intencao'


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