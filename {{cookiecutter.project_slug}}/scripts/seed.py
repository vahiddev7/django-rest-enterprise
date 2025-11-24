# --- seed.py ---
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
django.setup()

from modules.users.infrastructure.models import User

def run():
    User.objects.get_or_create(email='admin@example.com', first_name='Admin', last_name='User')

if __name__ == '__main__':
    run()