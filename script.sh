#!/bin/bash

set -ev

var=$(git diff --name-only HEAD...master)
echo "$var"

for filename in $var; do
	python script.py 
done

if [ "${TRAVIS_PULL_REQUEST}" = "true" ] && [ "$TRAVIS_BRANCH" == "prod" ]; then
	for filename in $var; do
		python scripts/deploy.py  
	done	
fi

