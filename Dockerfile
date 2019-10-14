ARG PYTHON_VERSION="3.6"
FROM python:${PYTHON_VERSION}-stretch AS builder

ARG NODE_VERSION="8.x"
RUN curl -sL "https://deb.nodesource.com/setup_${NODE_VERSION}" | bash - \
 && apt-get install --no-install-recommends -y \
      nodejs=8.16.0-1nodesource1

RUN apt-get install --no-install-recommends -y \
      unixodbc-dev=2.3.4-1

COPY src/server/static/package*.json /piaf/app/server/static/
RUN cd /piaf/app/server/static \
 && npm ci

COPY requirements.txt /
RUN pip install -r /requirements.txt \
 && pip wheel -r /requirements.txt -w /deps

COPY . /piaf

WORKDIR /piaf
RUN tools/ci.sh

FROM builder AS cleaner

RUN cd /piaf/app/server/static \
 && SOURCE_MAP=False DEBUG=False npm run build \
 && rm -rf components pages node_modules .*rc package*.json webpack.config.js

RUN cd /piaf \
 && python src/manage.py collectstatic --noinput

FROM python:${PYTHON_VERSION}-slim-stretch AS runtime

RUN apt-get update \
 && apt-get install --no-install-recommends -y \
      curl=7.52.1-5+deb9u9 \
      gnupg=2.1.18-8~deb9u4 \
      apt-transport-https=1.4.9
 && apt-get remove -y curl gnupg apt-transport-https \
 && rm -rf /var/lib/apt/lists/*

RUN useradd -ms /bin/sh piaf

COPY --from=builder /deps /deps
RUN pip install --no-cache-dir /deps/*.whl

COPY --from=cleaner --chown=piaf:piaf /piaf /piaf

ENV DEBUG="True"
ENV SECRET_KEY="change-me-in-production"
ENV PORT="8000"
ENV WORKERS="2"
ENV MATOMO_SITE_ID=""

USER piaf
WORKDIR /piaf
EXPOSE ${PORT}

CMD ["/piaf/tools/run.sh"]
