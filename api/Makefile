.ONESHELL:

install:
	poetry install

lock:
	poetry lock

test:
	pytest --no-migrations

check-migrations:
	python manage.py makemigrations --check --dry-run

migrate:
	python manage.py migrate

collectstatic:
	python manage.py collectstatic --noinput

check:
	black . --check \
	&& ruff check . \
	&& safety check \
	&& make check-migrations \

check-fix:
	black .
	ruff check --fix-only --show-fixes --statistics .

run:migrate collectstatic
	python manage.py runserver_plus 0.0.0.0:8000 --nostatic

celery-worker-run:
	celery -A weather_app worker

celery-beat-run:
	celery -A weather_app beat
