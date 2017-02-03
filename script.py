import frontmatter, pytest, sys, subprocess, git
from scripts.KBFrontmatter import KBFrontmatter

class KBValidator():

    repository = git.Git('./')
    base_branch = ''
    target_branch = ''

    def __init__(self, ):
        self.set_base()
        self.set_tartget()

    def gitDiff(self, branch1='', branch2=''):
        if branch1:
            self.set_base(branch1)
        if branch2:
            self.set_tartget(branch2)

        format = '--name-only'
        commits = []
        d = self.repository.diff('%s..%s' % ('HEAD', 'master'), format).split("\n")

        return d
    
    def set_base(self, base='HEAD'):
        if base:
            self.base_branch = base

        self.base_branch = self.repository.active_branch
    
    def set_tartget(self, target='master'):
        if target:
            self.target_branch = target

        self.target_branch = target


if __name__ == '__main__':
    # assuming 1 file at a time

    kb_validator = KBValidator()
    diff_files = kb_validator.gitDiff()
    print diff_files
    markup = KBFrontmatter()
    for c in diff_files:
        print '-- ' + c
        if c.endswith(('.md', '.markdown')):
            print '---> ' + c + ' - is markdown: Processing...'
            markup.set_filename(c)
            print markup.validate_markdown()
        else:
            print '---> ' + c + ' - is not markdown: Skipping'

  