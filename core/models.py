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



class TipoGosto(models.Model):
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'tipo_gosto'

    def __unicode__(self):
        return self.nome


class Perfil(models.Model):
    usuario = models.ForeignKey(User, related_name='perfil')
    CPF = models.CharField(max_length=11, blank=True, null=True)
    whatsapp = models.CharField(max_length=15, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    nacionalidade = models.CharField(max_length=50, blank=True, null=True)
    alugo_procuro = models.BooleanField(default=False)
    imagem = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'perfil'

    def __unicode__(self):
        return self.usuario.first_name


class TipoIntencao(models.Model):

    nome = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tipo_intencao'

    def __unicode__(self):
        return self.nome


class TipoBeneficio(models.Model):

    nome = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tipo_beneficio'

    def __unicode__(self):
        return self.nome


class TipoRegra(models.Model):

    nome = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tipo_regra'

    def __unicode__(self):
        return self.nome


class TipoItemIncluso(models.Model):

    nome = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tipo_item_incluso'

    def __unicode__(self):
        return self.nome

class TipoPeriodo(models.Model):

    nome = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tipo_periodo'

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
    imovel = models.ForeignKey(Imovel, related_name='visita')
    visitante = models.ForeignKey(User)
    data = models.DateTimeField()
    observacoes = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'imovel_has_visita'


class TipoValor(models.Model):
    nome = models.CharField(max_length=45, blank=True, null=True)
    tipo = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tipo_valor'

    def __unicode__(self):
        return self.nome

class Anuncio(models.Model):
    data_inicio = models.DateField()
    data_final = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    imovel = models.ForeignKey(Imovel, related_name='anuncio')

    class Meta:
        managed = True
        db_table = 'anuncio'

    def __unicode__(self):
        return "Anuncio:"+str(self.imovel_id)


class AnuncioHasInteressado(models.Model):
    anuncio = models.ForeignKey(Anuncio, related_name='interessado')
    interessado = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'anuncio_has_interessado'



class TipoData(models.Model):
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'tipo_data'

    def __unicode__(self):
        return str(self.tipo)


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
    perfil = models.ForeignKey(Perfil, related_name='gostos')
    gosto = models.ForeignKey(TipoGosto)

    class Meta:
        managed = True
        db_table = 'perfil_has_gostos'


class ImovelHasAvaliacao(models.Model):
    imovel = models.ForeignKey(Imovel, related_name='avaliacao')
    avaliador = models.ForeignKey(User)
    estrelas = models.IntegerField()
    mensagem = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'imovel_has_avaliacao'


class TipoLugarProximo(models.Model):
    nome = models.CharField(max_length=45, blank=True, null=True)
    tipo = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tipo_lugar_proximo'

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
    imovel = models.ForeignKey(Imovel, related_name='midia')

    class Meta:
        managed = True
        db_table = 'midia'

class ImovelHasLugarProximo(models.Model):
    imovel = models.ForeignKey(Imovel, related_name='proximo')
    lugar_proximo = models.ForeignKey(TipoLugarProximo)

    class Meta:
        managed = True
        db_table = 'imovel_has_lugar_proximo'

class ImovelHasBeneficio(models.Model):
    imovel = models.ForeignKey(Imovel, related_name='beneficio')
    beneficio = models.ForeignKey(TipoBeneficio)
    metro_quadrado = models.FloatField(blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'imovel_has_beneficio'

class ImovelHasRegra(models.Model):
    imovel = models.ForeignKey(Imovel, related_name='regra')
    regra = models.ForeignKey(TipoRegra)
    possibilidade = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'imovel_has_regra'

class ImovelHasItemIncluso(models.Model):
    imovel = models.ForeignKey(Imovel, related_name='incluso')
    item = models.ForeignKey(TipoItemIncluso)

    class Meta:
        managed = True
        db_table = 'imovel_has_item_incluso'


class ImovelHasPeriodo(models.Model):
    imovel = models.ForeignKey(Imovel, related_name='periodo')
    periodo = models.ForeignKey(TipoPeriodo)

    class Meta:
        managed = True
        db_table = 'imovel_has_periodo'


class ImovelHasValor(models.Model):
    imovel = models.ForeignKey(Imovel, related_name='valor')
    valor = models.ForeignKey(TipoValor)
    preco = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'imovel_has_valor'


class ImovelHasDisponibilidade(models.Model):
    imovel = models.ForeignKey(Imovel, related_name='disponibilidade')
    data = models.DateField()
    disponibilidade = models.ForeignKey(TipoData)

    class Meta:
        managed = True
        db_table = 'imovel_has_disponibilidade'


class ImovelIndicadoGosto(models.Model):
    imovel = models.ForeignKey(Imovel, related_name='imovelindicado')
    gosto = models.ForeignKey(TipoGosto)

    class Meta:
        managed = True
        db_table = 'imovel_indicado_gosto'


class ImovelIndicadoIntencao(models.Model):
    imovel = models.ForeignKey(Imovel, related_name='imovelintencao')
    intencao = models.ForeignKey(TipoIntencao)

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