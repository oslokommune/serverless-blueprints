Lambda Blueprint
=============
A blueprint to use as a starting point for lambda functions in Oslo Origo

# Usage
Copy repo content to your new repository, or create a new branch where you quickly can test a custom lambda function

# Setup
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

```
make init
```

# Tests

Tests are run using [tox](https://pypi.org/project/tox/): `make test`

For tests and linting we use [pytest](https://pypi.org/project/pytest/), [flake8](https://pypi.org/project/flake8/) and [black](https://pypi.org/project/black/).

# Deploy

`make deploy` or `make deploy-prod`

Requires `saml2aws`
