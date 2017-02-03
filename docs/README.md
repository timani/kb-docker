## Running the script Manually

### Run the script.py

This will detect the files that are a diff between master and the `HEAD` of the current branch

```
(venv) $ python script.py
[u'.travis.yml', u'file.txt', u'script.py', u'script.sh', u'scripts/__init__.py', u'scripts/deploy.py', u'scripts/frontmatter-test.1.py', u'scripts/frontmatter-test.py', u'scripts/how-to-test.py', u'tests/article_with_id.md', u'tests/article_without_id.md', u'tests/barebones.md', u'tests/fixtures/article_with_id.md', u'tests/fixtures/article_with_no_id.md', u'tests/fixtures/article_without_id.md', u'tests/fixtures/barebones.md']
-- .travis.yml
---> .travis.yml - is not markdown: Skipping
-- file.txt
---> file.txt - is not markdown: Skipping
-- script.py
---> script.py - is not markdown: Skipping
-- script.sh
---> script.sh - is not markdown: Skipping
-- scripts/__init__.py
---> scripts/__init__.py - is not markdown: Skipping
-- scripts/deploy.py
---> scripts/deploy.py - is not markdown: Skipping
-- scripts/frontmatter-test.1.py
---> scripts/frontmatter-test.1.py - is not markdown: Skipping
-- scripts/frontmatter-test.py
---> scripts/frontmatter-test.py - is not markdown: Skipping
-- scripts/how-to-test.py
---> scripts/how-to-test.py - is not markdown: Skipping
-- tests/article_with_id.md
---> tests/article_with_id.md - is markdown: Processing...
```

### Validate the article

Each article will be validated against the critieria to ensure the articles meet the Knowledge Base standards

```
************  Validating Article - tests/article_with_id.md **********

tests/article_with_id.md
This file does not exist in the current branch - has title
This file does not exist in the current branch - has template
This file does not exist in the current branch - has ID
This file does not exist in the current branch - has ID
-- tests/article_without_id.md
---> tests/article_without_id.md - is markdown: Processing...
...
```

### Handling errors

#### Invalid KB standards

If An article does not meet any of the criteria the error will be printed as part of the output

```
************  Validating Article - tests/fixtures/barebones.md **********

tests/fixtures/barebones.md
{}
*** Error: Article does not have a 'title' in the frontmatter
*** Error: Article does not have a 'template' in the frontmatter
*** Error: Article does not have a 'id' in the frontmatter
*** Error: Article does not have a 'locale' in the frontmatter

*************************

Failed: 6 errors Detected

************************
```

#### Diff in files between branches

If a diff has a file that exists in one branch but not in another the validation will be skipped

```
************  Validating Article - tests/article_with_id.md **********

tests/article_with_id.md
This file does not exist in the current branch - has title
This file does not exist in the current branch - has template
This file does not exist in the current branch - has ID
```
