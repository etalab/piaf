#!/usr/bin/env bash

set -o errexit

flake8
python src/manage.py migrate
coverage run --source=app src/manage.py test api.tests authentification.tests
coverage report

(cd src/server/static && npm run lint)
