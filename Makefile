DC    := 'docker-compose'
export WEBPACK_ENVIRONMENT_PRODUCTION=False

up:
	${DC} up

down:
	${DC} stop

restart: down up

build-statics:
	cd src/server/static && npm run build
