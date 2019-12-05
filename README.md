Lambda Boilerplate
==================
A boilerplate to use as a starting point for lambda functions in Oslo Origo


## Usage
Copy repo content to your new repository, or create a new branch where you
quickly can test a custom lambda function


## Setup

In these examples, we use the default `python3` distribution on your platform.
If you need a specific version of python you need to run the command for that
specific version. Ie. for 3.8 run `python3.8 -m venv .venv` instead to get a
virtualenv for that version.

### Installing global python dependencies

You can either install globally. This might require you to run as root (use sudo).

```bash
python3 -m pip install tox black pip-tools
```

Or, you can install for just your user. This is recommended as it does not
require root/sudo, but it does require `~/.local/bin` to be added to `PATH` in
your `.bashrc` or similar file for your shell. Eg:
`PATH=${HOME}/.local/bin:${PATH}`.

```bash
python3 -m pip install --user tox black pip-tools
```


### Installing local python dependencies in a virtualenv

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

```bash
make init
```


## Tests

Tests are run using [tox](https://pypi.org/project/tox/): `make test`

For tests and linting we use [pytest](https://pypi.org/project/pytest/),
[flake8](https://pypi.org/project/flake8/) and
[black](https://pypi.org/project/black/).


## Deploy

`make deploy` or `make deploy-prod`

Requires `saml2aws`


## IAM policy

IAM policy is available in
dataplatform-config/devops/modules/services/lambda-boilerplate/, but if you
want to copy-paste a IAM custom role while developing:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "LambdaBoilerplateS3GetObject",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject"
            ],
            "Resource": "arn:aws:s3:::ok-origo-dataplatform-dev/test/lambda-boilerplate/*"
        },
        {
            "Sid": "LambdaBoilerplateS3ListObjects",
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::ok-origo-dataplatform-dev"
        }
    ]
}
```
