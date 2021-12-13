# Serverless Python application blueprint

Blueprint for a "plain" Python application with a single simple Lambda function.

## Setup

```sh
make init
```

## Test

Tests are run using [tox](https://pypi.org/project/tox/):

```sh
make test
```

For tests and linting we use [pytest](https://pypi.org/project/pytest/),
[flake8](https://pypi.org/project/flake8/), and
[black](https://pypi.org/project/black/).

## Deploy

Example GitHub Actions for deploying to dev and prod on push to `main` is
included in `.github/workflows`.

You can also deploy from a local machine to dev (requires `saml2aws`) with:

```sh
make deploy
```

Or to prod with:

```sh
make deploy-prod
```
