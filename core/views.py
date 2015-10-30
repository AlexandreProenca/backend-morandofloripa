# coding: utf-8
from rest_auth.serializers import PasswordResetSerializer
from rest_framework.filters import DjangoFilterBackend
from rest_framework import permissions, viewsets, status, parsers, renderers
from django.contrib.auth.models import User
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
import models
import serializers

class UserView(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['username', 'email']


class TipoGostoView(viewsets.ModelViewSet):
    serializer_class = serializers.TipoGostoSerializer
    queryset = models.TipoGosto.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'nome', 'tipo']


class PerfilView(viewsets.ModelViewSet):
    serializer_class = serializers.PerfilSerializer
    queryset = models.Perfil.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'usuario', 'CPF', 'whatsapp', 'facebook', 'data_nascimento', 'sexo', 'nacionalidade', 'alugo_procuro']


class TipoIntencaoView(viewsets.ModelViewSet):
    serializer_class = serializers.TipoIntencaoSerializer
    queryset = models.TipoIntencao.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'nome', 'tipo']


class TipoBeneficioView(viewsets.ModelViewSet):
    serializer_class = serializers.TipoBeneficioSerializer
    queryset = models.TipoBeneficio.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'nome', 'tipo']


class TipoRegraView(viewsets.ModelViewSet):
    serializer_class = serializers.TipoRegraSerializer
    queryset = models.TipoRegra.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'nome', 'tipo']


class TipoItemInclusoView(viewsets.ModelViewSet):
    serializer_class = serializers.TipoItemInclusoSerializer
    queryset = models.TipoItemIncluso.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'nome', 'tipo']


class TipoPeriodoView(viewsets.ModelViewSet):
    serializer_class = serializers.TipoPeriodoSerializer
    queryset = models.TipoPeriodo.objects.all()
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

    filter_fields = ['id',
                     'metro_quadrado',
                     'bairro', 'nome_rua',
                     'numero_casa_ap',
                     'cep_imovel',
                     'observacoes',
                     'cidade',
                     'venda',
                     'disponivel',
                     'created',
                     'proprietario',
                     'tipo_imovel']

    def get_permissions(self):
        return (AllowAny() if self.request.method == 'GET' else IsAuthenticated()),

    def get_queryset(self):
        return models.Imovel.objects.prefetch_related(
            'midia',
            'beneficio',
            'valor',
            'visita',
            'avaliacao',
            'proximo',
            'beneficio',
            'regra',
            'incluso',
            'periodo',
            'valor',
            'disponibilidade',
            'imovelindicado',
            'imovelintencao'
        )

class ImovelHasVisitaView(viewsets.ModelViewSet):
    serializer_class = serializers.ImovelHasVisitaSerializer
    queryset = models.ImovelHasVisita.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'imovel', 'visitante', 'data', 'observacoes', 'created']


class TipoValorView(viewsets.ModelViewSet):
    serializer_class = serializers.TipoValorSerializer
    queryset = models.TipoValor.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'nome', 'tipo']


class AnuncioView(viewsets.ModelViewSet):
    serializer_class = serializers.AnuncioSerializer
    queryset = models.Anuncio.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'data_inicio', 'data_final', 'created', 'imovel']

    def get_permissions(self):
        return (AllowAny() if self.request.method == 'GET' else IsAuthenticated()),

    def get_queryset(self):
        return models.Anuncio.objects.prefetch_related('imovel')


class AnuncioHasInteressadoView(viewsets.ModelViewSet):
    serializer_class = serializers.AnuncioHasInteressadoSerializer
    queryset = models.AnuncioHasInteressado.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'anuncio', 'interessado', 'created']


class TipoDataView(viewsets.ModelViewSet):
    serializer_class = serializers.TipoDataSerializer
    queryset = models.TipoData.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'data', 'tipo']


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


class TipoLugarProximoView(viewsets.ModelViewSet):
    serializer_class = serializers.TipoLugarProximoSerializer
    queryset = models.TipoLugarProximo.objects.all()
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

    filter_fields = ['id', 'imovel', 'valor', 'preco']


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


class ImovelIndicadoIntencaoView(viewsets.ModelViewSet):
    serializer_class = serializers.ImovelIndicadoIntencaoSerializer
    queryset = models.ImovelIndicadoIntencao.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'imovel', 'intencao']


class PasswordReset(GenericAPIView):
    """
    Chama o método Django Auth PasswordResetForm save .
    Aceita os seguintes parâmetros
    POST : email
    Retorna o sucesso / falha mensagem ou e-mail , se não existir.
    """
    serializer_class = PasswordResetSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        # Create a serializer with request.DATA

        serializer = self.get_serializer(data=request.data)
        email = self.request.data['email']
        #
        if not User.objects.filter(email=email):
            return Response(data={"error": "Email " + email + " was not found"}, status=status.HTTP_400_BAD_REQUEST)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()

        # Return the success message with OK HTTP status
        return Response({"success": "Password reset e-mail has been sent."}, status=status.HTTP_200_OK)

password_reset = PasswordReset.as_view()