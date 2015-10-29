# coding: utf-8
from rest_framework import serializers
import models
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        write_only_fields = ('password',)

    # def update(self, attrs, instance=None):
    #     user = super(UserSerializer, self).update(attrs, instance)
    #     user.set_password(attrs['password'])
    #     return user



class GostoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gosto

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Perfil

class IntencaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Intencao

class BeneficioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Beneficio

class RegraSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Regra

class ItemInclusoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ItemIncluso

class PeriodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Periodo

class TipoImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TipoImovel



class ImovelHasVisitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImovelHasVisita

class ValorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Valor

class AnuncioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Anuncio

class AnuncioHasInteressadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AnuncioHasInteressado

class DisponibilidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Disponibilidade

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

class LugarProximoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LugarProximo

class MensagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mensagem

class MidiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Midia

class ImovelHasLugarProximoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImovelHasLugarProximo

class ImovelHasBeneficioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImovelHasBeneficio

class ImovelHasRegraSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImovelHasRegra

class ImovelHasItemInclusoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImovelHasItemIncluso

class ImovelHasPeriodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImovelHasPeriodo

class ImovelHasValorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImovelHasValor

class ImovelHasDisponibilidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImovelHasDisponibilidade

class ImovelIndicadoGostoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImovelIndicadoGosto

class ImovelSerializer(serializers.ModelSerializer):

    midia = MidiaSerializer()
    valor = ValorSerializer()

    class Meta:
        model = models.Imovel