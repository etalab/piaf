# Piaf, without Docker

This README is for devs who are not familiar with docker. Note that we do not recommend using Piaf without Docker: you may encounter issues, and if so feel free to open Issues in Github.

Most inforamtion will remain in the main [README.md](https://github.com/etalab/piaf) and here will only be listed the steps that differs.

## 1. Installation

First clone the repo:

```bash
git clone https://github.com/etalab/piaf.git
cd piaf
```

Then create the environment variables (you can customise your API keys and passwords):
```bash
cp .env-example .env
```

### Installing without Docker

As a prerequisite, you need to have installed on your computer:

* Python 3.6+
* Django 2.1.7+
* Node.js 8.0+
* Chromium (recommended)
* Vue cli 4.4+  (more info [here](https://cli.vuejs.org/guide/installation.html))


First install Python dependencies:

```bash
sudo apt-get install libpq-dev  # Linux/Debian only
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Secondly, install Vue cli (if needed):

```bash
sudo npm install -g @vue/cli@latest # In Linux/Debian
```

Then compile the frontend:

```bash
make build-statics
```

> When developing the frontend, you may prefer watching for files changes.
> Run `npm start` (instead of `npm run build`) for building and hot reloading.

## 2. Running


### Running without Docker

First prepare the database:

```bash
cd src
python manage.py migrate
```

Then create the admin user:

```bash
python manage.py create_admin --noinput --username "admin" --email "admin@example.com" --password "password"
```

And finally run the Django server:

```bash
python manage.py runserver
```

> Note that Django permits to run the server on a different IP or port. `python manage.py runserver <ip>:<port>`

## 3. Setting up your annotation campaign

See the main [README.md](https://github.com/etalab/piaf)

## 4. Annotation campaign

See the main [README.md](https://github.com/etalab/piaf)

## 5. Export results
See the main [README.md](https://github.com/etalab/piaf)

## 6. Configuration

## - General configuration

Passing most settings as environment variable will override the default settings. Here are some of the variable customisable:

```bash
DJANGO_ALLOW_SIGNUP=True # Allow users to singup (for crowdsourcing)
DJANGO_USE_MAILJET=False # use Mailjet or the native Django mail service
DJANGO_MAILJET_API_KEY=ffdfsfcfs2a00ad5ef367bfdsflsdk # put your Mailjet API key here, this is an example resulting in Errors
DJANGO_MAILJET_SECRET_KEY=nhf41cc0d45ffsdfs6fdsfdsffdsfsf # put your Mailjet API secret here, this is an example resulting in Errors
MATOMO_SITE_ID= # Matomo id
WEBPACK_ENVIRONMENT_PRODUCTION=False # build the frontend  or run a 'npm run serve'
```

### without Docker

Set the environment variable before launching your server
```
DEBUG=0 MATOMO_SITE_ID=77 src/manage.py runserver
```

this will disable debugging and activate Matomo tracking for instance, but all other ENV variable you want to customizr should be added in the previous line.

### - Special Configuration for the VueJS app

See the main [README.md](https://github.com/etalab/piaf)

## Troubleshooting & Contact

See the main [README.md](https://github.com/etalab/piaf)
