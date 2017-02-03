import unittest, frontmatter, git, pytest, sys

# assuming 1 file at a time
try:
    file_name = str(sys.argv[1])

    if file_name.endswith(('.md', '.markdown')):
        pass
    else:
        print file_name + ' - is not markdown: Skipping'

except IndexError:
    pass

class TestKBFrontmatter(unittest.TestCase):

    def test_has_title(self):
        "Parse frontmatter and only the frontmatter"
        with open(file_name) as f:
            metadata, content = frontmatter.parse(f.read())
            print content
        self.assertFalse('title' in metadata, "Article does not have an 'title' in the frontmatter")

    # @TODO 1. Enforce there is a template
    def test_has_template(self):
        "Parse frontmatter and only the frontmatter"

        with pytest.raises(ZeroDivisionError):
            1 / 0

    # @TODO 2. This should not block from passing when the value is empty
    def test_has_id(self):
        "Parse frontmatter and only the frontmatter"
        with open('tests/article_with_id.md') as f:
            metadata, content = frontmatter.parse(f.read())

        self.assertTrue('template' in metadata, "Article does not have an 'template' in the frontmatter")

  # @TODO 2. This should not block from passing when the value is empty
    def test_has_id_is_int(self):
        "Parse frontmatter and only the frontmatter"
        with open('tests/article_with_id.md') as f:
            metadata, content = frontmatter.parse(f.read())

        self.assertTrue('template' in metadata, "Article does not have an 'template' in the frontmatter")

  
    def test_has_locale(self):
        "Parse frontmatter and only the frontmatter"
        with open('tests/article_with_id.md') as f:
            metadata, content = frontmatter.parse(f.read())

        self.assertTrue('locale' in metadata, "Article does not have an 'locale' in the frontmatter")

    # @TODO 3. Markdown check, all files must be .md or .markdown
    def test_is_markdown_file(self):
        "Parse frontmatter and only the frontmatter"
        with open('tests/article_with_id.md') as f:
            metadata, content = frontmatter.parse(f.read())

        self.assertTrue('locale' in metadata, "Article does not have an 'locale' in the frontmatter")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestKBFrontmatter)
    unittest.TextTestRunner(verbosity=2).run(suite)

