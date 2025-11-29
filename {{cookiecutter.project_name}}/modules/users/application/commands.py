# --- commands.py ---
from modules.users.infrastructure.repositories import UserRepository

class RegisterUserCommand:
    def __init__(self, email, first_name='', last_name=''):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def execute(self):
        repo = UserRepository()
        existing = repo.get_by_email(self.email)
        if existing:
            raise ValueError('User already exists')
        return repo.create(email=self.email, first_name=self.first_name, last_name=self.last_name)