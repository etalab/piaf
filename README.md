# Piaf

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/b64ba7294eca479181b52d30a7d2e9d7)](https://app.codacy.com/app/guillim/piaf?utm_source=github.com&utm_medium=referral&utm_content=etalab/piaf&utm_campaign=Badge_Grade_Dashboard)

<abbr title="Pour Une IA Francophone">Piaf</abbr> is an open-source QA (question answering) annotation plateform.  
It handles the following features :  
* nice UI (conceived by a designer)
* contributor enrollment (signup & mail validation)
* contributor certification (by any member of the _admin_ team)
* _admin_ team administration (by the super-admin)
* input/output of texts to be annotated using the SQuAD format
* users scoring (for bot and troll removal)
* annotations managment


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


Now you have tow options : install the app with Docker or without

### Installing with Docker

As a prerequisite, you need to have installed Docker & Docker-compose on your computer.

Then, type:

```bash
docker-compose pull
```

### Installing without

See the dedicated [README_without_docker](https://github.com/etalab/piaf/blob/master/README_without_docker.md)

## 2. Running


### Running with Docker

```bash
make up
```
Note that it **takes a few minutes** to be up and reunning.  
Have a look at the Makefile for more details
### Running without

See the dedicated [README_without_docker](https://github.com/etalab/piaf/blob/master/README_without_docker.md)

## 3. Setting up your annotation campaign

### Reach the Admin panel
Open your web-browser at http://127.0.0.1:8000/login/ and login with the admin you created above (username: "admin", password: "password")

You will then be able to reach the admin panel, for any administration task you may require:
[127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)


### Import texts

We designed a simple interface for you to upload in an easy way your texts you want to annotate. It's located here : [/app/admin](http://127.0.0.1:8000/app/admin)

Here is an example of input dataset: [Click here to download](/input-dataset-example.json)

As you can see in the example above, texts have to match the [SQuAD](https://rajpurkar.github.io/SQuAD-explorer/) format. But, for additional app options, we accept some extra fields :
- __"categorie"__ : can be one of the followings - 'Religion', 'Géographie', 'Histoire', 'Sport', 'Arts', 'Société', 'Sciences' default to 'Société' if empty
- __"displaytitle"__ : if you need a more deligthful title (falls back to title if empty)
- __"reference"__ : integer like *7138870* for Wikipedia reference (falls back to 0 if empty)

## 4. Annotation campaign

Simply reach : [app/](http://127.0.0.1:8000/app/)  
And give your users this URL so they can begin to annotate.

#### Admin section

To manage users, you can reach the admin dashboard : [admin/](http://127.0.0.1:8000/admin/)

## 5. Export results

Once you have some annotated texts, you may want to download them so you can train your own QA model for instance. Please, download the result on the page : [app/admin](http://127.0.0.1:8000/app/admin)




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

### with Docker
Edit the .env file

### without
See the dedicated [README_without_docker](https://github.com/etalab/piaf/blob/master/README_without_docker.md)

### - Special Configuration for the VueJS app

There are some specific settings in a second `.env` file (it was simpler for us to keep two files). These settings are directly related with the frontend options. You will find it at this location : `src/piaf/front/.env`  

```bash
VUE_APP_ALLOW_ONBOARDING=true # Redirect new users to an onboarding process to teach them how to annotate a text
VUE_APP_PRINT_BRAVO=false # Option to hide the "Bravo" page after questions are submitted
```

## Troubleshooting & Contact

Feel free to [submit any feedback here](https://github.com/etalab/piaf/issues/new).

### Run VueJS app alone
It's possible to run the frontend application by itself. For this to work out, you will need :
- change `base: '/app'` into `base: '/'` in the file _src/piaf/front/src/router.js_
- make sure `publicPath: '/'` in the file _src/piaf/front/vue.config.js_
- to go to this folder _src/piaf/front_ & run `npm run watch`
- and start your server from _src/piaf/static/front_ where npm builds the app.


## Acknowledgements

PIAF plateform was originally inspired by [Doccano](https://github.com/chakki-works/doccano). The PIAF team contributed to Doccano repository until the Doccano project was to far from PIAF needs.

## License

2018 chakki.  
2019 DINUM, Guillim.  
2020 DINUM, Guillim.  
2021 DINUM, Guillim.  

This application is published under the MIT license.
