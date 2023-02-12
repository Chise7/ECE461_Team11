import sys, pytest, os
#sys.path.append("..")
from url import ramp_up

USERNAME =  'PC192'
TOKEN = os.getenv('GITHUB_TOKEN')
Testcases = [('Chise7', 'ECE461_Team11'),('words', 'double-metaphone'),('jonschlinkert', 'even'), ('SonarSource', 'chocolatey-packages'),('PSOPT', 'psopt'),('nullivex','nodist'),('cloudinary','cloudinary_npm'), ('lodash','lodash')]

def test_ramp_up():
    for cases in Testcases:
        validrampup = ramp_up.ramp_up(cases[0], cases[1], TOKEN)
        assert validrampup >= 0