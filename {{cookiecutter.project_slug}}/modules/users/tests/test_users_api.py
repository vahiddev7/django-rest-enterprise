# --- test_users_api.py ---
from django.urls import reverse
from rest_framework.test import APITestCase
from modules.users.infrastructure.models import User

class UsersAPITest(APITestCase):
    def setUp(self):
        User.objects.create(email='alice@example.com')

    def test_list_users_requires_auth(self):
        url = reverse('user-list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 401)