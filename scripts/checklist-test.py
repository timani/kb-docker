import unittest, frontmatter, git

class TestChecklistTemplate(unittest.TestCase):
   
     # @TODO 1. Enforce there is an title ## h1
    def test_has_title(self):
        try:
            pass
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

    # @TODO 2. Enforce there is an Environment ## h2
    def test_has_environment(self):
        return
 
    # @TODO 3. Enforce there is an Product (Product | Version) ## h2
    def test_has_product_version(self):
        return

    # @TODO 4. Enforce there is an Summary ## h2
    def test_has_summary(self):
        return

    # @TODO 5. Enforce there is an Checklist ## h2
    def test_has_checklist(self):   
        return