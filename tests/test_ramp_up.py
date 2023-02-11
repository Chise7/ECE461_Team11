import os
import pytest
from ..Run.ramp_up.ramp_up import *

USERNAME =  'PC192'
TOKEN = os.getenv('GITHUB_TOKEN')

@pytest.mark.url
def test_url_checker():
    # Just checks for general format, not contents
    validurl = url_checker('https://github.com/Perfare/AssetStudio')
    assert validurl == "Valid URL!"
    validurl = url_checker('https://grubhub.net/fungus/amogus')
    assert validurl == "Valid URL!"

    validurl = url_checker('youtube.com/watch?v=Qoa83DR2zhc')
    assert validurl == "Invalid URL!"
    validurl = url_checker('engineering.purdue.edu')
    assert validurl == "Invalid URL!"

@pytest.mark.npm
def test_npm_to_git_rep():
    realnpmdir = npm_to_git_rep('package/read-installed')
    assert realnpmdir == 'npm/read'
    realnpmdir = npm_to_git_rep('package/minimist')
    assert realnpmdir == 'minimistjs/minimist'


@pytest.mark.ramp_up
def test_ramp_up():
    validrampup = ramp_up()
