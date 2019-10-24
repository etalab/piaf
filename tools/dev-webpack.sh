#!/usr/bin/env bash

set -o errexit

root="$(dirname "$0")/.."
frontend="${root}/src/piaf/front/"

(
  cd "${frontend}"

  if [[ ! -d node_modules/.bin ]]; then
    echo "Installing dependencies"
    npm install
  fi

  echo "Starting npm run...  with WEBPACK_ENVIRONMENT_PRODUCTION = ${WEBPACK_ENVIRONMENT_PRODUCTION}"
  if [[ -n "${WEBPACK_ENVIRONMENT_PRODUCTION}" ]] && [[ "${WEBPACK_ENVIRONMENT_PRODUCTION}" = "True" ]]; then
    echo "--> building bundle for production"
    npm run build
    echo "--> build => bundle finished"
  else
    echo "--> starting to watch => hot-reload"
    npm run watch
    echo "--> watch with hot-reload ready"
  fi
)
