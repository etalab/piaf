#!/bin/bash

DC    := 'docker-compose'
export WEBPACK_ENVIRONMENT_PRODUCTION=True

up:
	if [[ ! -d "src/db" ]]; then \
		mkdir src/db; \
	fi; \
	${DC} up

down:
	${DC} stop

restart: down up

build-statics:
	if [[ -f "README.md" ]]; then \
		mkdir src/piaf/front/static; \
	fi; \
	cd src/piaf/front/static && npm run build

test:
	DATABASE_URL=pgsql://localhost/piaf?sslmode=disable src/manage.py test piaf

serve:
	DATABASE_URL=pgsql://localhost/piaf?sslmode=disable src/manage.py runserver
