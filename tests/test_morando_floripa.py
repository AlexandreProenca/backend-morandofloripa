# coding: utf-8
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory, APIClient

class TestAPIViews(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = User.objects.create_user('testuser@test.com', password='testing')
        self.user.save()
        self.token = Token.objects.filter(user=self.user)

    def _require_login(self):
        self.client.login(username='testuser', password='testing')

    def test_login_account(self):
        """
        Testa o login com um usuario de testes.
        """
        response = self.client.post(path='/rest-auth/login/', data={"username": 'testuser@test.com', "password": 'testing'}, format='json')
        self.assertEqual(response.status_code, 200, 'Expected Response Code 200, received {0} instead.'.format(response.status_code))
    #
    # def test_login_account_fail(self):
    #     """
    #     Testa o login nao autorizado com um usuario de testes.
    #     """
    #     response = self.client.post('/rest-auth/login/',
    #                                 {"username": 'testuser@test.com', "password": 'testings'},
    #                                 format='json')
    #
    #     self.assertEqual(response.status_code, 400,
    #         'Expected Response Code 400, received {0} instead.'.format(response.status_code))

