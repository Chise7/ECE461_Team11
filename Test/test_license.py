import sys
sys.path.insert(1, '../Run/URL_Fields')
import License

score = License.rustScore("GNU v2.1")
print(score)

def test_get_owner_repo():
    pass

def test_githubLicense():
    pass

def test_npm_to_git():
    pass

def test_searchReadme():
    pass

def test_fail_rustScore():
    pass

def test_pass_rustScore():
    pass