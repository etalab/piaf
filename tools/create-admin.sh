#!/usr/bin/env bash

if [[ "$#" -ne 3 ]]; then echo "Usage: $0 <username> <email> <password>" >&2; exit 1; fi

set -o errexit

python src/manage.py wait_for_db
python src/manage.py migrate
python src/manage.py create_admin --noinput --username="$1" --email="$2" --password="$3"
