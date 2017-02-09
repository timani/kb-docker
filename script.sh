#!/bin/bash

set -ev

var=$(git diff --name-only HEAD...master)
echo "$var"

python script.py

# @TODO Add a local variable for non-travis testing
 if [ "${TRAVIS_BRANCH}" == "prod" ]; then
	for filename in $var; do
		python scripts/deploy.py  
	done	
 fi

