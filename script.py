import frontmatter, pytest, sys, subprocess, git
from scripts import *

class KBValidator():

    file_name = ''

    def __init__(self, ):
        pass

    def gitDiff(self, branch1, branch2):
        format = '--name-only'
        commits = []
        g = git.Git('./')
        d = g.diff('%s..%s' % ('HEAD', 'master'), format).split("\n")

        return d

   # @TODO 1. Enforce there is a template
    def has_locale(self):
        "Parse frontmatter and only the frontmatter"
        with open(self.file_name) as f:
            metadata, content = frontmatter.parse(f.read())
            # print content
        if 'locale' in metadata:
            print  "+++ Success: Article has a 'locale' in the frontmatter - %s" % metadata['locale']                   
            return True
        else:
            print  "*** Error: Article does not have a 'locale' in the frontmatter"          
            return False

   # @TODO 1. Enforce there is a template
    def validate_markdown(self):
        print  "\n************  Validating Article - %s **********\n" % file_name                  
        kb.has_locale()  

if __name__ == '__main__':
    # assuming 1 file at a time

    kb_validator = KBValidator()
    diff_files = kb_validator.gitDiff('HEAD', 'master')
    print diff_files
    for c in diff_files:
        print '-- ' + c
        if c.endswith(('.md', '.markdown')):
            print '---> ' + c + ' - is markdown: Processing'
            kb_frontmatter = KBFrontmatter(c)
            kb_frontmatter.validate_markdown()
        else:
            print '---> ' + c + ' - is not markdown: Skipping'

  