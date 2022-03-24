.PHONY: help
SHELL:=/bin/bash

help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'


config-env:
	@cp contrib/env.exemple .env

build:
	docker-compose build

up: 
	docker-compose up
	
down: 
	docker-compose down

demo:
	docker-compose up -d
	docker-compose exec backend pipenv run python manage.py loaddata contrib/fixtures/initial_data.json

createsuperuser:
	docker-compose up -d
	docker-compose exec backend pipenv run python manage.py createsuperuser

tests:
	docker-compose up -d
	docker-compose exec -T backend pipenv run pytest

tests-cov:
	docker-compose up -d
	docker-compose exec -T backend pipenv run pytest --cov

flake8:
	docker-compose up -d
	docker-compose exec -T backend pipenv run flake8

pylint:
	docker-compose up -d
	docker-compose exec -T backend pipenv run pylint employee/
