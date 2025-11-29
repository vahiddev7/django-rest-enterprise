# --- test_auth_api.py ---
from django.urls import reverse
from rest_framework.test import APITestCase
from modules.users.infrastructure.models import User

class AuthAPITest(APITestCase):
    def setUp(self):
        User.objects.create(email='bob@example.com')

    def test_login_user(self):
        url = reverse('login')
        data = {'email': 'bob@example.com', 'password': 'pass'}
        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('token', resp.data)