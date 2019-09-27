#!/usr/bin/env bash

set -o errexit

if [[ ! -d "src/staticfiles" ]]; then python src/manage.py collectstatic --noinput; fi

python src/manage.py wait_for_db
python src/manage.py migrate
gunicorn --bind="0.0.0.0:${PORT:-8000}" --workers="${WORKERS:-1}" --pythonpath=app app.wsgi --timeout 300
