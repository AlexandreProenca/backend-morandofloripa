# coding: utf-8
from rest_framework import serializers
import models
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        write_only_fields = ('password',)

    def update(self, attrs, instance=None):
        user = super(UserSerializer, self).update(attrs, instance)
        user.set_password(attrs['password'])
        return user



class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Avaliacao

class ImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Imovel

class LugarProximoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LugarProximo

class MensagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mensagem

class MidiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Midia

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Perfil
