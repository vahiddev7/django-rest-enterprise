# --- backends.py ---
from django.contrib.auth.backends import BaseBackend
from modules.users.infrastructure.models import User

class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=email)
            if user.is_active:
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        from modules.users.infrastructure.models import User
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None