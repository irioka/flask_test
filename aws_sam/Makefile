S3_BUCKET = dge-serverless-test
PIPELINE = -pipeline
STACK = -analysis
REGION = ap-northeast-1
REPOSITORY = dge-xxx-dev
EMAIL = irioka@digitalge.com

TEST_STACK = $(STACK)-test


.PHONY: all create-bucket clean build test-package test-deploy delete-test-stack cicd-package cicd-deploy

all: clean build test-package test-deploy test

create-bucket:
	aws s3api create-bucket --bucket $(S3_BUCKET) --create-bucket-configuration LocationConstraint=$(REGION)

clean:
	$(MAKE) -C $(SUMMARIZER) clean

build:
	$(MAKE) -C $(SUMMARIZER)

test:
	$(MAKE) -C $(SUMMARIZER) test

package:
	npm run package

test-deploy: test-package
	aws cloudformation deploy \
		--template-file ./packaged-template.yml \
		--stack-name $(TEST_STACK) \
		--capabilities CAPABILITY_IAM \
		--parameter-overrides `cat test-stack-configuration.json | jq -r '.Parameters | to_entries | map("\(.key)=\(.value|tostring)") | .[]' | tr '\n' ' ' | awk '{print}'` \
				"S3BucketName=$(S3_BUCKET)" \
		--region $(REGION)

delete-test-stack:
	aws cloudformation delete-stack --stack-name $(TEST_STACK) --region $(REGION)

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
