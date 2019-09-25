DC    := 'docker-compose'

up:
	${DC} up

down:
	${DC} stop

restart: down up

up-dev:
	export WEBPACK_ENVIRONMENT_PRODUCTION=False
	${DC} up

down-dev:
	${DC} stop

restart-dev: down-dev up-dev
