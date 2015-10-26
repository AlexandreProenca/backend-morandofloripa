# coding: utf-8
from rest_auth.serializers import PasswordResetSerializer
from rest_framework.filters import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import permissions, viewsets, status, parsers, renderers
from django.contrib.auth.models import User
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
import models
import serializers



class UserView(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['username', 'email']

    def get_permissions(self):
        return (AllowAny() if self.request.method == 'POST' else IsAuthenticated()),



class AvaliacaoView(viewsets.ModelViewSet):
    serializer_class = serializers.AvaliacaoSerializer
    queryset = models.Avaliacao.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'de', 'estrelas', 'mensagem', 'imovel', 'like']


class ImovelView(viewsets.ModelViewSet):
    serializer_class = serializers.ImovelSerializer
    queryset = models.Imovel.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'tipo', 'whatsapp_contato', 'telefone_contato', 'email_contato', 'metro_quadrado', 'valor_diaria', 'valor_mensal', 'periodo_anual', 'periodo_temporada', 'qt_quartos', 'qt_garagem', 'qt_moradores', 'aceita_animais', 'aceita_sexo', 'aceita_criancas', 'aceita_tabaco', 'aceita_tocar_instrumento', 'aceita_visita_de_amigos', 'aceita_festas', 'alugado', 'unica_terreno', 'mobilhado', 'possue_vigilacia', 'possue_ar_condicionado', 'possue_sacada', 'possue_maq_lavar', 'possue_fogao', 'possue_geladeira', 'possue_microondas', 'possue_churrasqueira', 'possue_banheiro_externo', 'possue_cama', 'possue_liquidificador', 'possue_grill', 'possue_torradeira', 'possue_mesa', 'possue_orta', 'possue_piscina', 'possue_tv_cabo', 'possue_garagem', 'possue_tv', 'incluso_internet', 'incluso_luz', 'incluso_agua', 'incluso_tv_cabo', 'disponivel_a_partir_de', 'disponivel_ate', 'horario_visita_inicio', 'horario_visita_fim', 'bairro', 'nome_rua', 'numero_casa_ap', 'cep_imovel', 'observacoes', 'cidade', 'valor_medio_agua_por_morador', 'valor_medio_luz_por_morador', 'valor_medio_internet_por_morador', 'valor_medio_aluguel_por_morador', 'valor_max_aluguel_morador', 'alugo_ou_procuro', 'created', 'proprietario']


class LugarProximoView(viewsets.ModelViewSet):
    serializer_class = serializers.LugarProximoSerializer
    queryset = models.LugarProximo.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'nome', 'tipo', 'created', 'imovel']


class MensagemView(viewsets.ModelViewSet):
    serializer_class = serializers.MensagemSerializer
    queryset = models.Mensagem.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'de', 'titulo', 'mensagem', 'created', 'imovel']


class MidiaView(viewsets.ModelViewSet):
    serializer_class = serializers.MidiaSerializer
    queryset = models.Midia.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'link', 'tipo', 'created', 'imovel']


class PerfilView(viewsets.ModelViewSet):
    serializer_class = serializers.PerfilSerializer
    queryset = models.Perfil.objects.all()
    filter_backends = [DjangoFilterBackend]

    filter_fields = ['id', 'user', 'curte_skate', 'curte_long_bord', 'curte_surf', 'curte_kite', 'curte_sup', 'curte_praia', 'curte_balada', 'curte_sussego', 'curte_natureza', 'curte_escalada', 'estuda_na_ufsc', 'estuda_na_udesc', 'curte_slackline', 'curte_mergulho', 'curte_montanha', 'curte_nadar', 'curte_bike', 'curte_organicos', 'curte_cerveja_caseira', 'curte_paraquedismo', 'curte_parapente', 'curte_kayake', 'curte_animais', 'data_nascimento', 'direcao_trabalho', 'created']


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

        serializer = self.get_serializer(data=request.DATA)
        email = self.request.DATA[unicode('email')]

        if not User.objects.filter(email=email):
            return Response(data={"error": "Email " + email + " not found"}, status=status.HTTP_400_BAD_REQUEST)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()

        # Return the success message with OK HTTP status
        return Response({"success": "Password reset e-mail has been sent."}, status=status.HTTP_200_OK)

password_reset = PasswordReset.as_view()
