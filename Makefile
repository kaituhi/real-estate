# Check if the `.env` file exists in the current directory.
ifneq (,&(wildcard ./.env))
# If `.env` exists, include it and set an environment variable with the `.env` file path.
include .env
export ENV_FILE_PARAM = --env-file .env 

endif

# Target to build and start the docker containers in detached mode (background).
build:
	docker-compose up --build -d --remove-orphans

# Target to start the docker containers in detached mode (background) without rebuilding.
up:
	docker-compose up -d

# Target to stop and remove the docker containers.
down:
	docker-compose down

# Target to show the logs from docker containers.
show-logs:
	docker-compose logs

# Target to run Django migrations inside the `api` service.
migrate:
	docker-compose exec api python3 manage.py migrate

# Target to create new Django migrations inside the `api` service.
makemigrations:
	docker-compose exec api python3 manage.py makemigrations

# Target to create a superuser for the Django admin inside the `api` service.
superuser:
	docker-compose exec api python3 manage.py createsuperuser

# Target to collect static files in Django inside the `api` service (with no input).
collectstatic:
	docker-compose exec api python3 manage.py collectstatic --no-input --clear

# Target to stop and remove docker containers along with their volumes.
down-v:
	docker-compose down -v

# Target to inspect the `estate-src_postgres_data` docker volume.
volume:
	docker volume inspect real-estate_postgres_data

# Target to run psql commands inside the `postgres-db` service (connecting to the `estate` database).
estate-db:
	docker-compose exec postgres-db psql --username=admin --dbname=estate

# Target to run the `pytest` tests inside the `api` service, with coverage reporting (no warnings).
test:
	docker-compose exec api pytest -p no:warnings --cov=.

# Target to run `pytest` tests inside the `api` service, with coverage report in HTML format.
test-html:
	docker compose exec api pytest -p no:warnings --cov=. --cov-report html

# Target to run `flake8` for code linting inside the `api` service.
flake8:
	docker-compose exec api flake8 .

# Target to check if the code is formatted with `black` inside the `api` service.
black-check:
	docker-compose exec api black --check --exclude=migrations .

# Target to see a diff of formatting changes suggested by `black` inside the `api` service.
black-diff:
	docker compose exec api black --diff --exclude=migrations .

# Target to auto-format the code using `black` inside the `api` service.
black:
	docker-compose exec api black --exclude=migrations .

# Target to check the import order using `isort` inside the `api` service (without making changes).
isort-check:
	docker-compose exec api isort . --check-only --skip env --skip migrations

# Target to show the diff of import order changes suggested by `isort` inside the `api` service.
isort-diff:
	docker-compose exec api isort . --diff --skip env --skip migrations

# Target to auto-format import order using `isort` inside the `api` service.
isort:
	docker-compose exec api isort . --skip env --skip migrations