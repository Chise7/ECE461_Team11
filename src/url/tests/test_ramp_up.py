import sys, pytest, os
#sys.path.append("..")
from url import ramp_up

USERNAME =  'PC192'
#TOKEN = os.getenv('GITHUB_TOKEN')
TOKEN = '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'
Testcases = [('Chise7', 'ECE461_Team11'),('words', 'double-metaphone'),('jonschlinkert', 'even'), ('apache', 'airflow'),('PSOPT', 'psopt'),('nullivex','nodist'),('cloudinary','cloudinary_npm'), ('PC192','ChubbyChecker')]

def test_ramp_up():
    for cases in Testcases:
        validrampup = ramp_up.ramp_up(cases[0], cases[1], TOKEN)
        assert validrampup >= 0
def test_ramp_up_exception():
    for cases in Testcases:
        validrampup = ramp_up.ramp_up(cases[0], cases[1]+"bungo", TOKEN)
        assert validrampup < 0