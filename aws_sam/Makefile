SERVERLESS = node_modules/.bin/sls
S3_BUCKET = dge-serverless-test
REGION = ap-northeast-1
PIPELINE = serverless-test-pipeline
STACK = serverless-test
REPOSITORY = dge-serverless-test
EMAIL = irioka@digitalge.com


.PHONY: all create-bucket dev-package dev-deploy dev-remove cicd-package cicd-deploy

all: test dev-deploy

create-bucket:
	aws s3api create-bucket --bucket $(S3_BUCKET) --create-bucket-configuration LocationConstraint=$(REGION)

package:
	$(SERVERLESS) package --s3_bucket $(S3_BUCKET)

dev-deploy:
	$(SERVERLESS) deploy --s3_bucket $(S3_BUCKET)

dev-remove:
	$(SERVERLESS) remove --s3_bucket $(S3_BUCKET)

test:
	$(MAKE) -C $(SUMMARIZER) test

cicd-package: cicd-template.yml
	aws cloudformation package \
		--template-file ./cicd-template.yml \
		--s3-bucket $(S3_BUCKET) \
		--output-template-file packaged-cicd-template.yml

cicd-deploy: cicd-package
	aws cloudformation deploy \
			--template-file ./packaged-cicd-template.yml \
			--stack-name $(PIPELINE) \
			--capabilities CAPABILITY_IAM \
			--parameter-overrides \
					"PipelineName=$(PIPELINE)" \
					"S3Bucket=$(S3_BUCKET)" \
					"RepositoryName=$(REPOSITORY)" \
					"StackName=$(STACK)" \
					"Email=$(EMAIL)" \
			--region $(REGION)
