#!/usr/bin/env bash

set -o errexit

root="$(dirname "$0")/.."
frontend="${root}/src/server/static"

(
  cd "${frontend}"

  if [[ ! -d node_modules/.bin ]]; then
    echo "Installing dependencies"
    npm install
  fi

  echo "Starting webpack"
  if [[ -n "${WEBPACK_ENVIRONMENT_PRODUCTION}" ]] && [[ "${WEBPACK_ENVIRONMENT_PRODUCTION}" = "True" ]]; then
    npm run build
    echo "webpack build => bundle finished"
  else
    echo "webpack starting in dev-mode with hot-reload"
    npm start
  fi
)
