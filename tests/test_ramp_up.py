import os
import pytest
from ..src.url.ramp_up import *

USERNAME =  'PC192'
TOKEN = os.getenv('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')
Testcases = [('Chise7', 'ECE461_Team11'),('words', 'double-metaphone'),('jonschlinkert', 'even-metaphone'), ...
            ('SonarSource', 'chocolatey-packages'),('PSOPT', 'psopt'),('nullivex','nodist'),('cloudinary','cloudinary_npm'), ...
            ('lodash','lodash')]

@pytest.mark.correct_ramp_up
def test_ramp_up():
    for cases in Testcases:
        validrampup = ramp_up(cases[0], cases[1], TOKEN)
        assert validrampup >= 0
