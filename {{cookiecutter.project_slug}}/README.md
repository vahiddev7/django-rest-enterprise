# --- README.md ---
# {{cookiecutter.project_name}}

This is an enterprise Django REST template with the following features:
- Users module
- Authentication module
- Multi-database support
- Dockerized setup (Django, Celery, Redis, Nginx)
- Ready for production and development
- DRF + drf-spectacular for API docs

## Quick Start
1. Copy `.env.example` to `.env` and update values
2. Build Docker containers: `docker-compose up --build`
3. Apply migrations: `docker-compose run django python manage.py migrate`
4. Create superuser: `docker-compose run django python manage.py createsuperuser`
5. Seed initial data: `docker-compose run django python scripts/seed.py`
6. Access API at `http://localhost:8000/api/`

## Testing
Run tests with `docker-compose run django pytest -s`
        init_db.sh
        seed.py