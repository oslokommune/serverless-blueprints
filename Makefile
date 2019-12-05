.AWS_ROLE_NAME ?= oslokommune/iamadmin-SAML

.DEV_ACCOUNT := ***REMOVED***
.PROD_ACCOUNT := ***REMOVED***

.DEV_ROLE := 'arn:aws:iam::$(.DEV_ACCOUNT):role/$(.AWS_ROLE_NAME)'
.PROD_ROLE := 'arn:aws:iam::$(.PROD_ACCOUNT):role/$(.AWS_ROLE_NAME)'

.DEV_PROFILE := saml-origo-dev
.PROD_PROFILE := saml-dataplatform-prod

PYTHON := python3

.PHONY: init
init:
	npm install

.PHONY: pip-install
pip-install:
	$(PYTHON) -m pip install tox black pip-tools wheel twine bump2version

.PHONY: format
format:
	$(PYTHON) -m black .

.PHONY: test
test:
	$(PYTHON) -m tox -p auto

.PHONY: upgrade-deps
upgrade-deps:
	pip-compile -U

.PHONY: deploy
deploy: init format test login-dev
	sls deploy --stage $${STAGE:-dev} --aws-profile $(.DEV_PROFILE)

.PHONY: deploy-prod
deploy-prod: init format is-git-clean test login-prod
	sls deploy --stage prod --afws-profile $(.PROD_PROFILE)

.PHONY: undeploy
undeploy: login-dev
	sls remove --stage $${STAGE} --aws-profile $(.DEV_PROFILE)

.PHONY: login-dev
login-dev:
	saml2aws login --role=$(.DEV_ROLE) --profile=$(.DEV_PROFILE)

.PHONY: login-prod
login-prod:
	saml2aws login --role=$(.PROD_ROLE) --profile=$(.PROD_PROFILE)

.PHONY: is-git-clean
is-git-clean:
	@status=$$(git fetch origin && git status -s -b) ;\
	if test "$${status}" != "## master...origin/master"; then \
		echo; \
		echo Git working directory is dirty, aborting >&2; \
		false; \
	fi

.PHONY: build
build: init
	$(PYTHON) setup.py sdist bdist_wheel

.PHONY: jenkins-bump-patch
jenkins-bump-patch: is-git-clean
	bump2version patch
	git push origin HEAD:${BRANCH_NAME}
