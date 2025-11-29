# --- __init__.py ---
{% if cookiecutter.use_celery.lower() == 'y' %}
from config.celery import app as celery_app

__all__ = ("celery_app",)
{% endif %}
