import jwt
from django.contrib.auth import authenticate
from django.conf import settings
from datetime import datetime, timedelta


class AuthService:
    def authenticate_user(self, username, password):
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            return None

        payload = {
            "user_id": user.id,
            "username": user.username,
            "email": user.email,
            "exp": datetime.utcnow() + timedelta(seconds=settings.JWT_EXP_DELTA_SECONDS)
        }
        token = jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
        return {"token": token, "user": {"id": user.id, "username": user.username}}