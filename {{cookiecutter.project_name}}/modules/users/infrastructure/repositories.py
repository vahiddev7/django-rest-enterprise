# --- repositories.py ---
from .models import User

class UserRepository:
    def get_by_email(self, email):
        return User.objects.using('default').filter(email=email).first()

    def create(self, **data):
        return User.objects.using('default').create(**data)