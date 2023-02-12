import sys, pytest, os
from url import ramp_up

USERNAME =  'PC192'
TOKEN = os.getenv('GITHUB_TOKEN')
Testcases = [('Chise7', 'ECE461_Team11'),('words', 'double-metaphone'),('jonschlinkert', 'even'), ('apache', 'airflow'),('PSOPT', 'psopt'),('nullivex','nodist'),('cloudinary','cloudinary_npm'), ('PC192','ChubbyChecker')]

def test_ramp_up():
    for cases in Testcases:
        validrampup = ramp_up.ramp_up(cases[0], cases[1], TOKEN)
        assert validrampup >= 0
def test_ramp_up_exception():
    for cases in Testcases:
        validrampup = ramp_up.ramp_up(cases[0], cases[1]+"bungo", TOKEN)
        assert validrampup < 0
