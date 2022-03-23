#!/bin/bash
cp ./.contrib/env.exemple .env
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate
case $ENV in local | dev | test ) \
        echo "[running fixtures]" && \
        pipenv run python manage.py loaddata data.json;; esac
pipenv run python manage.py runserver 0.0.0.0:8000
sleep 2