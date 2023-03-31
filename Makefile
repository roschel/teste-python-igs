virtualvenv:
	python3 -m venv venv && source venv/bin/activate

migrate:
	python3 manage.py migrate

create-user:
	python3 manage.py createsuperuser --username 'admin' --email 'admin@email.com'

build:
	docker build -t test-django . && docker run -d --name django-web -p 8000:8000 test-django:latest