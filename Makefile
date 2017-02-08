.PHONY: all plan apply destroy provision ssh

TEST_BRANCH = $(RAND) 

# Default command
all: plan apply provision

deploy: apply

centos-ami-ids:
	./bin/nbb centos-ami-ids

install-dependencies:
	./bin/nbb install-dependencies

test-main: test-init test-run

test-init: 
    git checkout -b $(TEST_BRANCH) \
    echo $TEST_BRANCH

test-run:
	python script.py

test-clean:
	git branch -d bar

# Image Makefile tasks
build-image:
	docker build -t pivotal-gss/kb-docker .

clean:
	rm *o hellofactorial.cpp

