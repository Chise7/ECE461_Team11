import sys, pytest
#sys.path.append("..")
from url import ramp_up

USERNAME =  'PC192'
TOKEN = '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'
Testcases = [('Chise7', 'ECE461_Team11'),('words', 'double-metaphone'),('jonschlinkert', 'even'), ('SonarSource', 'chocolatey-packages'),('PSOPT', 'psopt'),('nullivex','nodist'),('cloudinary','cloudinary_npm'), ('lodash','lodash')]

def test_ramp_up():
    for cases in Testcases:
        validrampup = ramp_up.ramp_up(cases[0], cases[1], TOKEN)
        assert validrampup >= 0