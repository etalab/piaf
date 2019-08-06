# Piaf

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/b64ba7294eca479181b52d30a7d2e9d7)](https://app.codacy.com/app/guillim/piaf?utm_source=github.com&utm_medium=referral&utm_content=etalab/piaf&utm_campaign=Badge_Grade_Dashboard)
[![Build Status](https://travis-ci.org/etalab/piaf.svg?branch=master)](https://travis-ci.org/etalab/piaf)

Piaf est un projet d'annotation de texte open-source spécialisé sur la quesiton réponse. Il a été construit à partir du projet [Doccano](https://github.com/chakki-works/doccano) => un grand merci à l'équipe de Doccano.

## Prérequis

* Python 3.6+
* Django 2.1.7+
* Node.js 8.0+
* Google Chrome(recommandé)

## Installation

D'abord cloner le repo:

```bash
git clone https://github.com/etalab/piaf.git
cd piaf
```

Puis, 2 options sont possibles:

**Option1: Avec Docker-Compose** [recommandé]

```bash
docker-compose pull
```

**Option2: Setup Python environment**

Installer les dépendances python:

```bash
sudo apt-get install libpq-dev
pip install -r requirements.txt
cd app
```

Puis lancer le server webpack pour compiler le frontend en continue:

```bash
cd server/static
npm install
npm run build
# npm start  # for developers
cd ..
```

## Utilisation

### Lancer le server de development

Let’s start the development server and explore it.

Depending on your installation method, there are two options:

**Option1: Docker-Compose** [recommandé]

```bash
docker-compose up
```

**Option2: Lancer le server de dévelopment Django**

```bash
python manage.py migrate
```

Puis il faut créer le premier utilisateur, l'admin:

```bash
python manage.py create_admin --noinput --username "admin" --email "admin@example.com" --password "password"
```

Les développeurs pourront lancer des tests si besoin: (optionel)

```bash
python manage.py test server.tests
```

Enfin, lancer le server:

```bash
python manage.py runserver
```

Changer ip & port si besoin: (optionel)
```bash
python manage.py runserver <ip>:<port>
```


Puis ouvrir votre navigateur <http://127.0.0.1:8000/login/>. Vous devriez voir:

<img src="./docs/login_form.png" alt="Login Form" width=400>

### Création d'un projet

Une fois connecté en tant qu'admin vous pouvez créer un projet:

<img src="./docs/projects.png" alt="projects" width=600>

Cliquer sur le boutton `Create Project`:

<img src="./docs/create_project.png" alt="Project Creation" width=400>

Ici, vous aurez la possiblilité de créer plusieurs type de projet. Seul le projet de **question-réponse** à de la valeur ici, si vous êtes intéressés par d'autres type de projet, vous devriez visiter le projet [doccano](https://github.com/chakki-works/doccano) dont est issue Piaf.

### Importer des textes

Cliquer sur `Import Data`:

<img src="./docs/upload.png" alt="Upload project" width=600>

Deux types de fichiers peuvent être importés:
- `CSV file`: doit avoir un header avec une colonne `text` ou alors, être un fichier mono-colonne.
- `JSON file`: chaque ligne doit être un objet JSON avec une clé `text` key. le format de JSON permet d'avoir des rendu type **line breaks**.

`example.csv` (or `example.txt`)
```python
EU rejects German call to boycott British lamb.
He lives in Newark, Ohio.
...
```
`example.json`
```JSON
{"text": "EU rejects German call to boycott British lamb."}
{"text": "He lives in Newark, Ohio."}
...
```

Toute autre colonne (ou clé pour JSON) sont enregistrés en metadata.

### Annotation

Cliquer sur le boutton `Annotate Data` dans la barre de navigation:

<img src="./docs/annotation.png" alt="Edit label" width=600>

### Exportation des résultats

Après une phase d'annotation, vous avez la possibilité de télécharger les résutlats annotés. Clicquer sur `Export Data`. Vous verrez alors l'écran:

<img src="./docs/export_data.png" alt="Edit label" width=600>  


Les formats possibles sont JSON et CSV

Note sur les meta-data:  
Tous les documents ont une colonne de metadata, qui contient les données du document importé. La principale utilité de ces meta-data est de pouvoir reconcilier les résultats exportés avec ceux du système original. Par example:

`import.json`
```JSON
{"text": "EU rejects German call to boycott British lamb.", "external_id": 1}
```
`output.json`
```JSON
{"doc_id": 16, "text": "EU rejects calls", "labels": ["news"], "username": "user23", "metadata": {"external_id": 1}}
```

## Contact

Les feedback sont les bienvenues: [soumettre une remarque](https://github.com/etalab/piaf/issues/new).
