## I can't install piaf.

Following list is ordered by from easy to hard. If you are not familiar with Python development, please consider easy setup.

1. [One click deployment to Cloud Service.](https://github.com/etalab/piaf#deployment)
   * Only you have to do is create an account. Especially [Heroku](https://www.heroku.com/home) does not require your credit card (if free plan).
   * [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
   * [![AWS CloudFormation Launch Stack SVG Button](https://cdn.rawgit.com/buildkite/cloudformation-launch-stack-button-svg/master/launch-stack.svg)](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://s3-external-1.amazonaws.com/cf-templates-10vry9l3mp71r-us-east-1/20190732wl-new.templatexloywxxyimi&stackName=piaf)
   * > Notice: (1) EC2 KeyPair cannot be created automatically, so make sure you have an existing EC2 KeyPair in one region. Or [create one yourself](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html#having-ec2-create-your-key-pair). (2) If you want to access piaf via HTTPS in AWS, here is an [instruction](https://github.com/etalab/piaf/wiki/HTTPS-setting-for-piaf-in-AWS).
2. [Use Docker](https://docs.docker.com/install/)
   * Docker doesn't bother you by the OS, Python version, etc problems. Because an environment for application is packed as a container.
   * Get piaf's image: `docker pull etalab/piaf`
   * Create & Run piaf container: `docker run -d --name piaf -p 8000:80 etalab/piaf`
   * Create a user: `docker exec piaf tools/create-admin.sh "admin" "admin@example.com" "password"`
   * Stop piaf container: `docker stop piaf`
   * Re-Launch piaf container: `docker start piaf`
3. Install from source
   * **I want to remember you that this is the hardest setup way. You have to install Python/Node.js and type many commands.**
   * [Install Python](https://www.python.org/downloads/)
   * [Install Node.js](https://nodejs.org/en/download/)
   * Get the source code of piaf: `git clone https://github.com/etalab/piaf.git`
   * Move to piaf directory: `cd piaf`
   * Create environment for piaf: `virtualenv venv`
   * Activate environment: `source venv/bin/activate`
   * Install required packages: `pip install -r requirements.txt`
   * Move server directory: `cd src/server`
   * Build frontend library: `npm install`
   * Build frontend source code: `npm run build`
   * Back to server directory: `cd ../`
   * Initialize piaf: `python manage.py migrate`
   * Create user: `python manage.py createsuperuser`
   * Run piaf: `python manage.py runserver`
   * Stop piaf: Ctrl+C
   * Re-Launch piaf: `python manage.py runserver` (Confirm you are at `src/server` directory and environment is active).

## I can't upload my data.

Please check the following list.

- File encoding: `UTF-8` is appropriate.
- Filename: alphabetic file name is suitable.
- File format selection: File format radio button should be selected properly.
- When you are using JSON/JSONL: Confirm JSON data is valid.
  - You can use [JSONLint](https://jsonlint.com/) or some other tool (when JSONL, pick one data and check it).
- When you are using CSV: Confirm CSV data is valid.
  - You can use Excel or some tools that have import CSV feature.
- Lack of line: Data file should not contain blank line.
- Lack of field: Data file should not contain blank field.

**You don't need your real & all data to validate file format. The picked data & masked data is suitable if your data is large or secret.**

## I want to add annotators.

* You can create other annotators by [Django Admin site](https://djangobook.com/django-admin-site/).
