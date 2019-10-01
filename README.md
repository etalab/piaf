# Piaf

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/b64ba7294eca479181b52d30a7d2e9d7)](https://app.codacy.com/app/guillim/piaf?utm_source=github.com&utm_medium=referral&utm_content=etalab/piaf&utm_campaign=Badge_Grade_Dashboard)
[![Build Status](https://travis-ci.org/etalab/piaf.svg?branch=master)](https://travis-ci.org/etalab/piaf)

<abbr title="Pour Une IA Francophone">Piaf</abbr> is an open-source annotation project specialized in questions/answers.
I was built based on [Doccano](https://github.com/chakki-works/doccano) => a big thanks to the Doccano team.

## Prerequirements

* Python 3.6+
* Django 2.1.7+
* Node.js 8.0+
* Chromium (recommended)

## Installation

First clone the repo:

```bash
git clone https://github.com/etalab/piaf.git
cd piaf
```

Then choose either to run the app through Docker-Compose or manually

### Installing through Docker-Compose

```bash
docker-compose pull
```

## Installing manually

First install Python dependencies:

```bash
sudo apt-get install libpq-dev  # Linux/Debian only
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then compile the frontend:

```bash
make build-statics
```

> When developing the frontend, you may prefer watching for files changes.
> Run `npm start` (instead of `npm run build`) for building and hot reloading.

## Running

### Running the server for development

Let’s start the development server and explore it.
Depending on your installation method above, there are two options:

### Running through Docker-Compose

```bash
docker-compose up
```

### Running Django manually

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

## Creating a project

Open your web-browser at http://127.0.0.1:8000/login/ and login with the admin you created above (username: "admin", password: "password"):

<img src="./docs/login_form.png" alt="Login Form" width=400>

You will then access the home screen:

<img src="./docs/projects.png" alt="projects" width=600>


You can create various kinds of projects. Onle the **questions/answers** project is considered here.
If you are interested in others kinds of projects you should visit [doccano](https://github.com/chakki-works/doccano) from which Piaf is forked.


### Running the tests

```bash
python manage.py test server.tests
```


### Importing texts

Click on `Import Data`:

<img src="./docs/upload.png" alt="Upload project" width=600>

2 types of files can be imported:
- `CSV file`: must include a header with a "text" column or must be a single column file.
- `JSON file`: each row must be a JSON object including a "text" key. Note that JSON format is line-breaks friendly.

`example.csv` (or `example.txt`):

```python
EU rejects German call to boycott British lamb.
He lives in Newark, Ohio.
...
```

`example.json`:

```JSON
{"text": "EU rejects German call to boycott British lamb."}
{"text": "He lives in Newark, Ohio."}
...
```

If any other column (or key in a JSON file) is present they are saved as _metadata_.

### Annotation

Click in the _Annotate Data_ button in the navigation bar:

<img src="./docs/annotation.png" alt="Edit label" width=600>


### Exporing results

After annotating you can download the annotated results.
Click on "Export Data".

You will see a similar screen:

<img src="./docs/export_data.png" alt="Edit label" width=600>

Possible formats are CSV or JSON.

> All documents have a _metadata_ column which contain data about the imported document.
> These _metadata_ are especially useful to match imported results with the original dataset.
> Example:

`import.json`:

```JSON
{"text": "EU rejects German call to boycott British lamb.", "external_id": 1}
```

`output.json`:

```JSON
{"doc_id": 16, "text": "EU rejects calls", "labels": ["news"], "username": "user23", "metadata": {"external_id": 1}}
```

## Contact

Feel free to [submit any feedback](https://github.com/etalab/piaf/issues/new).
