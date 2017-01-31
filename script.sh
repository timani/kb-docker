#!/bin/bash
set -ev

CHANGED_FILES=$(git diff --name-only master...bar)
echo "$var"

for filename in "$CHANGED_FILES"; do
	pytest scripts/frontmatter-test.py -v    
done

exit


if [ "${TRAVIS_PULL_REQUEST}" = "true" ] && [ "$TRAVIS_BRANCH" == "prod" ]; then
	for filename in $CHANGED_FILES; do
		python scripts/deploy.py  
	done	
fi

