# --- usecases.py ---
from modules.authentication.domain.services import AuthService

class LoginUser:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def execute(self):
        service = AuthService()
        result = service.authenticate_user(self.username, self.password)
        if not result:
            raise ValueError("Invalid credentials")
        return result