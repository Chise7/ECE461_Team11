import os

import pytest
from ..src.ramp_up.ramp_up import *

USERNAME =  'PC192'
TOKEN = os.getenv('GITHUB_TOKEN')

@pytest.mark.url
def test_url_checker():
    validurl = url_checker()
@pytest.mark.npm
def test_npm_to_git_rep():
    realnpmdir = npm_to_git_rep()
@pytest.mark.ramp_up
def test_ramp_up():
    validrampup = ramp_up()
