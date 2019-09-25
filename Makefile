DC    := 'docker-compose'
export WEBPACK_ENVIRONMENT_PRODUCTION=False

up:
	${DC} up

down:
	${DC} stop

restart: down up

build-statics:
	cd app/server/static && npm run build
