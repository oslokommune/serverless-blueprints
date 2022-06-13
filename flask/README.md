# Serverless Flask application blueprint

[Flask](https://flask.palletsprojects.com) application as a single Lambda
function.  Based on an example from
<https://serverless.com/blog/flask-python-rest-api-serverless-lambda-dynamodb/>.

## Test

Tests are run using [tox](https://pypi.org/project/tox/):

```sh
make test
```

For tests and linting we use [pytest](https://pypi.org/project/pytest/),
[flake8](https://pypi.org/project/flake8/), and
[black](https://pypi.org/project/black/).

## Run

`make run` to start up Flask app locally.

## Deploy

Example GitHub Actions for deploying to dev and prod on push to `main` is
included in `.github/workflows`.

You can also deploy from a local machine to dev with:

```sh
make deploy
```

Or to prod with:

```sh
make deploy-prod
```
