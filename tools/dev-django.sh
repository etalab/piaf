#!/usr/bin/env bash

set -o errexit

root="$(dirname "$0")/.."
app="${root}/src"
venv="${root}/venv"

if [[ ! -f "${venv}/bin/python" ]]; then
  echo "Creating virtualenv"
  mkdir -p "${venv}"
  python3 -m venv "${venv}"
  "${venv}/bin/pip" install --upgrade pip setuptools
fi

echo "Installing dependencies"
"${venv}/bin/pip" install -r "${root}/requirements.txt"

echo "Initializing database"
"${venv}/bin/python" "${app}/manage.py" wait_for_db
"${venv}/bin/python" "${app}/manage.py" migrate

if [[ -n "${ADMIN_USERNAME}" ]] && [[ -n "${ADMIN_PASSWORD}" ]] && [[ -n "${ADMIN_EMAIL}" ]]; then
  "${venv}/bin/python" "${app}/manage.py" create_admin \
    --username "${ADMIN_USERNAME}" \
    --password "${ADMIN_PASSWORD}" \
    --email "${ADMIN_EMAIL}" \
    --noinput \
  || true
fi

PORT="8000"
WORKERS="2"
echo "so now ============="
echo "${venv}/bin/sh" ls

if [[ ${DJANGO_ENVIRONMENT_PRODUCTION} = "True" ]]; then
  echo "Starting django in Production mode"
  "${venv}/bin/gunicorn" --bind="0.0.0.0:${PORT:-8000}" --workers="${WORKERS:-1}" --pythonpath='/src,/src/src' app.wsgi --timeout 300
else
  echo "Starting django in Development mode"
  "${venv}/bin/python" -u "${app}/manage.py" runserver "$@"
fi
