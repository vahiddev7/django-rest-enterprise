# --- production.py ---
from .base import *
DEBUG = False
SECURE_SSL_REDIRECT = True


LOGGING["loggers"]["django"]["level"] = "WARNING"
LOGGING["loggers"]["modules"]["level"] = "INFO"

LOGGING["handlers"]["file"]["filename"] = os.path.join(BASE_DIR, "logs/prod.log")