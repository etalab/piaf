DC    := 'docker-compose'
export WEBPACK_ENVIRONMENT_PRODUCTION=False

up:
	${DC} up

down:
	${DC} stop

restart: down up

build-statics:
	cd src/piaf/front/static && npm run build
