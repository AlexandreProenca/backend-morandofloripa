# coding: utf-8
from rest_framework import serializers
import models
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        write_only_fields = ('password',)
        exclude = ('password', 'is_staff', 'last_login', 'is_superuser', 'username', 'date_joined')


class TipoGostoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TipoGosto
        exclude = ('id',)

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Perfil

class TipoIntencaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TipoIntencao
        exclude = ('id', 'tipo')

class TipoBeneficioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TipoBeneficio
        exclude = ('id', 'tipo')

class TipoRegraSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TipoRegra
        exclude = ('id', 'tipo')

class TipoItemInclusoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TipoItemIncluso
        exclude = ('id', 'tipo')

class TipoPeriodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TipoPeriodo
        exclude = ('id', 'tipo')

class TipoImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TipoImovel
        exclude = ('id', 'tipo')

class ImovelHasVisitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImovelHasVisita
        exclude = ('imovel', 'id')
        depth = 1

class TipoValorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TipoValor

class AnuncioHasInteressadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AnuncioHasInteressado

class TipoDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TipoData
        exclude = ('id', 'tipo')

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Endereco

class TelefoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Telefone

class PerfilHasGostosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PerfilHasGostos

class ImovelHasAvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImovelHasAvaliacao
        exclude = ('imovel', 'id')
        depth = 1

class TipoLugarProximoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TipoLugarProximo
        exclude = ('id', 'tipo')

class MensagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mensagem

class MidiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Midia
        exclude = ('imovel', 'id')

class ImovelHasLugarProximoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImovelHasLugarProximo
        exclude = ('imovel', 'id')
        depth = 1

class ImovelHasBeneficioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImovelHasBeneficio
        exclude = ('imovel', 'id')
        depth = 1

class ImovelHasRegraSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImovelHasRegra
        exclude = ('imovel', 'id')
        depth = 1

class ImovelHasItemInclusoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImovelHasItemIncluso
        exclude = ('imovel', 'id')
        depth = 1

class ImovelHasPeriodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImovelHasPeriodo
        exclude = ('imovel', 'id')
        depth = 1

class ImovelHasValorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImovelHasValor
        exclude = ('imovel', 'id')
        depth = 1

class ImovelHasDisponibilidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImovelHasDisponibilidade
        depth = 1
        exclude = ('imovel', 'id')

class ImovelIndicadoGostoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImovelIndicadoGosto
        depth = 1
        exclude = ('imovel', 'id')

class ImovelIndicadoIntencaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImovelIndicadoIntencao
        depth = 1
        exclude = ('imovel', 'id')

class ImovelSerializer(serializers.ModelSerializer):

    tipo_imovel = TipoImovelSerializer()
    proprietario = UserSerializer()
    midia = MidiaSerializer(many=True)
    beneficio = ImovelHasBeneficioSerializer(many=True)
    valor = ImovelHasValorSerializer(many=True)
    disponibilidade = ImovelHasDisponibilidadeSerializer(many=True)
    visita = ImovelHasVisitaSerializer(many=True)
    avaliacao = ImovelHasAvaliacaoSerializer(many=True)
    proximo = ImovelHasLugarProximoSerializer(many=True)
    regra = ImovelHasRegraSerializer(many=True)
    incluso = ImovelHasItemInclusoSerializer(many=True)
    periodo = ImovelHasPeriodoSerializer(many=True)
    imovelindicado = ImovelIndicadoGostoSerializer(many=True)
    imovelintencao = ImovelIndicadoIntencaoSerializer(many=True)

    class Meta:
        model = models.Imovel

class AnuncioSerializer(serializers.ModelSerializer):

    imovel = ImovelSerializer()

    class Meta:

        model = models.Anuncio
        depth = 2