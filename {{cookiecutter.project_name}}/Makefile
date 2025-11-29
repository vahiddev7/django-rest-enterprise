# --- Makefile ---
    
run:
	python manage.py runserver

migrate:
	python manage.py migrate

createsuperuser:
	python manage.py createsuperuser

format:
	isort . && black .

test:
	pytest -s