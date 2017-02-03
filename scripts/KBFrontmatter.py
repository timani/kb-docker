import frontmatter, git, pytest, sys


class KBFrontmatter():

    file_name = ''
    is_valid = False

    def set_filename(self, file_name):
        self.file_name = file_name

    def has_title(self):
        "Parse frontmatter and only the frontmatter"
        with open(self.file_name) as f:
            metadata, content = frontmatter.parse(f.read())
            print metadata
        if 'title' in metadata:
            print  "+++ Success: Article has a 'title' in the frontmatter - %s" % metadata['title']                   
            return True
        else:
            print  "*** Error: Article does not have a 'title' in the frontmatter"          
            return False

   # @TODO 1. Enforce there is a template
    def has_template(self):
        "Parse frontmatter and only the frontmatter"
        with open(self.file_name) as f:
            metadata, content = frontmatter.parse(f.read())
            # print content
        if 'template' in metadata:
            print  "+++ Success: Article has a 'template' in the frontmatter - %s" % metadata['template']                   
            return True
        else:
            print  "*** Error: Article does not have a 'template' in the frontmatter"          
            return False

   # @TODO 1. Enforce there is a template
    def has_id(self):
        "Parse frontmatter and only the frontmatter"
        with open(self.file_name) as f:
            metadata, content = frontmatter.parse(f.read())
            # print content
        if 'id' in metadata:
            print  "+++ Success: Article has a 'id' in the frontmatter - %s" % metadata['id']                   
            return True
        else:
            print  "*** Error: Article does not have a 'id' in the frontmatter"          
            return False
 
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
        print  "\n************  Validating Article - %s **********\n" % self.file_name                  
        if self.has_title():
            self.is_valid = True
        if not self.has_template():
            self.is_valid = True
        if not self.has_id():
            self.is_valid = False
        if not self.has_locale():
            self.is_valid = False

        return self.is_valid

if __name__ == '__main__':
    # assuming 1 file at a time
    if len(sys.argv) > 1:
        file_name = str(sys.argv[1])
        if file_name.endswith(('.md', '.markdown')):
            print file_name + ' - is markdown: Processing'
            kb = KBFrontmatter(file_name)
            kb.validate_markdown()
        else:
            print file_name + ' - is not markdown: Skipping'
    else:
        print 'No file specified. \nExample Command:'
        print '\n python scripts/frontmatter-test.py article.md'

    
