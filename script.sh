#!/bin/bash

set -ev

#TESTING
python script.py
python scripts/deploy.py

var=$(git diff --name-only HEAD...master)
echo "$var"

for filename in $var; do
	python script.py 
done

# @TODO Add a local variable for non-travis testing
 if [ "${TRAVIS_PULL_REQUEST}" = "true" ] && [ "$TRAVIS_BRANCH" == "prod" ]; then
	for filename in $var; do
		python scripts/deploy.py  
	done	
 fi

