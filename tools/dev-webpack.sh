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

  echo "Starting npm run..."
  if [[ -n "${WEBPACK_ENVIRONMENT_PRODUCTION}" ]] && [[ "${WEBPACK_ENVIRONMENT_PRODUCTION}" = "True" ]]; then
    npm run build
    echo "--> build => bundle finished"
  else
    echo "--> watch | dev-mode with hot-reload"
    npm run watch
  fi
)
