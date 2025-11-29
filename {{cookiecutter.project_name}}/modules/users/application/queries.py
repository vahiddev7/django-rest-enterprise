# --- queries.py ---
from modules.users.infrastructure.repositories import UserRepository

class GetUserByEmailQuery:
    def __init__(self, email):
        self.email = email

    def execute(self):
        repo = UserRepository()
        return repo.get_by_email(self.email)