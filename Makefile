DC    := 'docker-compose'
export WEBPACK_ENVIRONMENT_PRODUCTION=False

up:
	${DC} up

down:
	${DC} stop

restart: down up
