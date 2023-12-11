from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token

class AuthTestCase(TestCase):

    def setUp(self):
        self.user_client = User.objects.create_user(username='voter1', password='123')
        self.admin_user = User.objects.create_user(username='admin', password='admin')
        self.admin_user.is_superuser = True
        self.admin_user.save()

    def test_login(self):
        data = {'username': 'voter1', 'password': '123'}
        response = self.client.post(reverse('login'), data, format='json')
        self.assertEqual(response.status_code, 200)

        token = Token.objects.get(user__username='voter1')
        self.assertTrue(token.key)

    def test_login_fail(self):
        data = {'username': 'voter1', 'password': '321'}
        response = self.client.post(reverse('login'), data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_getuser(self):
        data = {'username': 'voter1', 'password': '123'}
        response = self.client.post(reverse('login'), data, format='json')
        self.assertEqual(response.status_code, 200)

        token = Token.objects.get(user__username='voter1')
        response = self.client.post(reverse('getUser'), {'token': token.key}, format='json')
        self.assertEqual(response.status_code, 200)

        user = response.json()
        self.assertEqual(user['id'], self.user_client.id)
        self.assertEqual(user['username'], 'voter1')



    def test_register(self):
        data = {'username': 'admin', 'password': 'admin'}
        response = self.client.post(reverse('login'), data, format='json')
        self.assertEqual(response.status_code, 200)

        token = Token.objects.get(user__username='admin')
        headers = {'Content-Type': 'text/html'}
        response = self.client.post(reverse('Autenticacion'), {'token': token.key, 'username': 'user1', 'password': 'pwd1'}, format='json', **headers)
        self.assertEqual(response.status_code, 200)
        

    def test_logout(self):
        data = {'username': 'voter1', 'password': '123'}
        response = self.client.post(reverse('login'), data, format='json')
        self.assertEqual(response.status_code, 200)

        token = Token.objects.get(user__username='voter1')
        response = self.client.post(reverse('logout'), {'token': token.key}, format='json')
        self.assertEqual(response.status_code, 200)

        # Verifica que el token se haya eliminado después del cierre de sesión
        with self.assertRaises(Token.DoesNotExist):
            Token.objects.get(user__username='voter1')

    def test_register_bad_permissions(self):
        data = {'username': 'voter1', 'password': '123'}
        response = self.client.post(reverse('login'), data, format='json')
        self.assertEqual(response.status_code, 200)

        token = Token.objects.get(user__username='voter1')
        response = self.client.post(reverse('getUser'), {'token': token.key, 'username': 'user1'}, format='json')
        self.assertEqual(response.status_code, 200)

    def test_register_bad_request(self):
        data = {'username': 'admin', 'password': 'admin'}
        response = self.client.post(reverse('login'), data, format='json')
        self.assertEqual(response.status_code, 200)

        token = Token.objects.get(user__username='admin')
        response = self.client.post(reverse('getUser'), {'token': token.key, 'username': 'user1'}, format='json')
        self.assertEqual(response.status_code, 200)

    def test_register_user_already_exist(self):
        data = {'username': 'admin', 'password': 'admin'}
        response = self.client.post(reverse('login'), data, format='json')
        self.assertEqual(response.status_code, 200)

        token = Token.objects.get(user__username='admin')
        response = self.client.post(reverse('getUser'), {'token': token.key, 'username': 'admin'}, format='json')
        self.assertEqual(response.status_code, 200)

