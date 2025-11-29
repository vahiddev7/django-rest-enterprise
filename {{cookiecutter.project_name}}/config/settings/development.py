# --- development.py ---
from .base import *
DEBUG = True

LOGGING["handlers"]["console"]["formatter"] = "simple"
LOGGING["loggers"]["django"]["level"] = "DEBUG"
LOGGING["loggers"]["modules"]["level"] = "DEBUG"