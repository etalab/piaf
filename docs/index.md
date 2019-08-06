# Welcome to piaf

## Text Annotation for Human

piaf is an open source text annotation tool for human. It provides annotation features for text classification, sequence labeling and sequence to sequence. So, you can create labeled data for sentiment analysis, named entity recognition, text summarization and so on. Just create project, upload data and start annotation. You can build dataset in hours.


## Demo

You can enjoy [annotation demo](http://piaf.herokuapp.com).

### [Named entity recognition](https://piaf.herokuapp.com/demo/named-entity-recognition/)

First demo is one of the sequence labeling tasks, named-entity recognition. You just select text spans and annotate it. Since piaf supports shortcut key, so you can quickly annotate text spans.

![Named Entity Recognition](./named_entity_annotation.gif)

### [Sentiment analysis](https://piaf.herokuapp.com/demo/text-classification/)

Second demo is one of the text classification tasks, topic classification. Since there may be more than one category, you can annotate multi-labels.

![Text Classification](./text_classification.gif)

### [Machine translation](https://piaf.herokuapp.com/demo/translation/)

Final demo is one of the sequence to sequence tasks, machine translation. Since there may be more than one responses in sequence to sequence tasks, you can create multi responses.

![Machine Translation](./translation.gif)

## Quick Deployment

### Heroku

piaf can be deployed to [Heroku](https://www.heroku.com/) by clicking on the button below:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Of course, you can deploy piaf by using [heroku-cli](https://devcenter.heroku.com/articles/heroku-cli).

```bash
heroku create
heroku stack:set container
git push heroku master
```

### AWS

piaf can be deployed to AWS ([Cloudformation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)) by clicking on the button below:

[![AWS CloudFormation Launch Stack SVG Button](https://cdn.rawgit.com/buildkite/cloudformation-launch-stack-button-svg/master/launch-stack.svg)](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://s3-external-1.amazonaws.com/cf-templates-10vry9l3mp71r-us-east-1/20190732wl-new.templatexloywxxyimi&stackName=piaf)

> Notice: (1) EC2 KeyPair cannot be created automatically, so make sure you have an existing EC2 KeyPair in one region. Or [create one yourself](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html#having-ec2-create-your-key-pair). (2) If you want to access piaf via HTTPS in AWS, here is an [instruction](https://github.com/chakki-works/piaf/wiki/HTTPS-setting-for-piaf-in-AWS).
