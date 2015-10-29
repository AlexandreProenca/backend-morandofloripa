# coding: utf-8
from rest_framework.filters import DjangoFilterBackend
from rest_framework import viewsets
from django.contrib.auth.models import User
import models
import serializers


class UserView(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['username', 'email']


class GostoView(viewsets.ModelViewSet):
    serializer_class = serializers.GostoSerializer
    queryset = models.Gosto.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'nome']


class PerfilView(viewsets.ModelViewSet):
    serializer_class = serializers.PerfilSerializer
    queryset = models.Perfil.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'usuario', 'CPF', 'whatsapp', 'facebook', 'data_nascimento', 'sexo', 'nacionalidade', 'alugo_procuro']


class IntencaoView(viewsets.ModelViewSet):
    serializer_class = serializers.IntencaoSerializer
    queryset = models.Intencao.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'nome', 'tipo']


class BeneficioView(viewsets.ModelViewSet):
    serializer_class = serializers.BeneficioSerializer
    queryset = models.Beneficio.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'nome', 'tipo']


class RegraView(viewsets.ModelViewSet):
    serializer_class = serializers.RegraSerializer
    queryset = models.Regra.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'nome', 'tipo']


class ItemInclusoView(viewsets.ModelViewSet):
    serializer_class = serializers.ItemInclusoSerializer
    queryset = models.ItemIncluso.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'nome', 'tipo']


class PeriodoView(viewsets.ModelViewSet):
    serializer_class = serializers.PeriodoSerializer
    queryset = models.Periodo.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'nome', 'tipo']


class TipoImovelView(viewsets.ModelViewSet):
    serializer_class = serializers.TipoImovelSerializer
    queryset = models.TipoImovel.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'nome', 'tipo']


class ImovelView(viewsets.ModelViewSet):
    serializer_class = serializers.ImovelSerializer
    queryset = models.Imovel.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'metro_quadrado', 'bairro', 'nome_rua', 'numero_casa_ap', 'cep_imovel', 'observacoes', 'cidade', 'venda', 'disponivel', 'created', 'proprietario', 'tipo_imovel']


class ImovelHasVisitaView(viewsets.ModelViewSet):
    serializer_class = serializers.ImovelHasVisitaSerializer
    queryset = models.ImovelHasVisita.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'imovel', 'visitante', 'data', 'observacoes', 'created']


class ValorView(viewsets.ModelViewSet):
    serializer_class = serializers.ValorSerializer
    queryset = models.Valor.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'nome', 'tipo']


class AnuncioView(viewsets.ModelViewSet):
    serializer_class = serializers.AnuncioSerializer
    queryset = models.Anuncio.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'data_inicio', 'data_final', 'created', 'imovel']


class AnuncioHasInteressadoView(viewsets.ModelViewSet):
    serializer_class = serializers.AnuncioHasInteressadoSerializer
    queryset = models.AnuncioHasInteressado.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'anuncio', 'interessado', 'created']


class DisponibilidadeView(viewsets.ModelViewSet):
    serializer_class = serializers.DisponibilidadeSerializer
    queryset = models.Disponibilidade.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'data_inicio', 'data_final']


class EnderecoView(viewsets.ModelViewSet):
    serializer_class = serializers.EnderecoSerializer
    queryset = models.Endereco.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'cidade', 'bairro', 'rua', 'complemento', 'cep', 'tipo', 'perfil']


class TelefoneView(viewsets.ModelViewSet):
    serializer_class = serializers.TelefoneSerializer
    queryset = models.Telefone.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'numero', 'ddd', 'tipo', 'operadora', 'perfil']


class PerfilHasGostosView(viewsets.ModelViewSet):
    serializer_class = serializers.PerfilHasGostosSerializer
    queryset = models.PerfilHasGostos.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'perfil', 'gosto']


class ImovelHasAvaliacaoView(viewsets.ModelViewSet):
    serializer_class = serializers.ImovelHasAvaliacaoSerializer
    queryset = models.ImovelHasAvaliacao.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'imovel', 'avaliador', 'estrelas', 'mensagem', 'created']


class LugarProximoView(viewsets.ModelViewSet):
    serializer_class = serializers.LugarProximoSerializer
    queryset = models.LugarProximo.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'nome', 'tipo']


class MensagemView(viewsets.ModelViewSet):
    serializer_class = serializers.MensagemSerializer
    queryset = models.Mensagem.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'de', 'para', 'titulo', 'mensagem', 'enviada', 'visualizada', 'created']


class MidiaView(viewsets.ModelViewSet):
    serializer_class = serializers.MidiaSerializer
    queryset = models.Midia.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'link', 'tipo', 'imovel']


class ImovelHasLugarProximoView(viewsets.ModelViewSet):
    serializer_class = serializers.ImovelHasLugarProximoSerializer
    queryset = models.ImovelHasLugarProximo.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'imovel', 'lugar_proximo']


class ImovelHasBeneficioView(viewsets.ModelViewSet):
    serializer_class = serializers.ImovelHasBeneficioSerializer
    queryset = models.ImovelHasBeneficio.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'imovel', 'beneficio', 'metro_quadrado', 'quantidade']


class ImovelHasRegraView(viewsets.ModelViewSet):
    serializer_class = serializers.ImovelHasRegraSerializer
    queryset = models.ImovelHasRegra.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'imovel', 'regra', 'possibilidade']


class ImovelHasItemInclusoView(viewsets.ModelViewSet):
    serializer_class = serializers.ImovelHasItemInclusoSerializer
    queryset = models.ImovelHasItemIncluso.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'imovel', 'item']


class ImovelHasPeriodoView(viewsets.ModelViewSet):
    serializer_class = serializers.ImovelHasPeriodoSerializer
    queryset = models.ImovelHasPeriodo.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'imovel', 'periodo']


class ImovelHasValorView(viewsets.ModelViewSet):
    serializer_class = serializers.ImovelHasValorSerializer
    queryset = models.ImovelHasValor.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'imovel', 'valor']


class ImovelHasDisponibilidadeView(viewsets.ModelViewSet):
    serializer_class = serializers.ImovelHasDisponibilidadeSerializer
    queryset = models.ImovelHasDisponibilidade.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'imovel', 'disponibilidade']


class ImovelIndicadoGostoView(viewsets.ModelViewSet):
    serializer_class = serializers.ImovelIndicadoGostoSerializer
    queryset = models.ImovelIndicadoGosto.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'imovel', 'gosto']

