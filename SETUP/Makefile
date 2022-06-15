.PHONY: help login init set-cors destroy gen-key
.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

login: ## Run GCloud and Pulumi logins
	pulumi logout
	pulumi login
	gcloud auth login
	gcloud auth application-default login

init: ## Create google project and pulumi stack
	gcloud projects create cdp-albuquerque-4009e905 --set-as-default
	pulumi stack init cdp-albuquerque-4009e905

set-cors: ## Set cors for the bucket
	gsutil cors set cors.json gs://cdp-albuquerque-4009e905.appspot.com/

destroy: ## Fully teardown Pulumi and GCloud
	pulumi stack rm cdp-albuquerque-4009e905 --force
	gcloud projects delete cdp-albuquerque-4009e905
	rm -f .keys/cdp-albuquerque-4009e905.json

gen-key: ## Generate a service account JSON
	mkdir .keys/ -p
	gcloud iam service-accounts create cdp-albuquerque-4009e905 \
    	--description="CDP Dev Service Account for $(USER)" \
    	--display-name="cdp-albuquerque-4009e905"
	gcloud projects add-iam-policy-binding cdp-albuquerque-4009e905 \
    	--member="serviceAccount:cdp-albuquerque-4009e905@cdp-albuquerque-4009e905.iam.gserviceaccount.com" \
		--role="roles/owner"
	gcloud iam service-accounts keys create .keys/cdp-albuquerque-4009e905.json \
  		--iam-account "cdp-albuquerque-4009e905@cdp-albuquerque-4009e905.iam.gserviceaccount.com"