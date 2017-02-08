import frontmatter, pytest, sys, subprocess, git
from src.KBFrontmatter import KBFrontmatter
from src.KBValidator import KBValidator


if __name__ == '__main__':
    # Validate all the files in commit
    kb_validator = KBValidator()

    # List the files that are different between HEAD..master
    diff_files = kb_validator.git_diff()
    print diff_files

    # Validate the KB frontmatter
    markup = KBFrontmatter()
    # Loop through the files
    for c in diff_files:
        print '-- ' + c
        # Validate the file is markdown
        if c.endswith(('.md', '.markdown')):
            print '---> ' + c + ' - is markdown: Processing...'
            markup.set_filename(c)
            markup.validate_markdown()
        else:
            print '---> ' + c + ' - is not markdown: Skipping'
    
    if markup.is_valid:
        print "\n*************************\n"
        print "Failed: %d errors Detected" % markup.is_valid
        print "\n************************\n"
        exit()

    # print kb_validator.is_valid