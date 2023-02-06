from urllib.parse import urlparse
from URL_Fields import licenseScore
#from URL_Fields import correctnessScore
import sys
import json
#from github import Github
import ndjson
import ctypes
#rustLib = ctypes.CDLL("target/debug/rustlib.dll")
#netFunc = rustLib.net_score

def main_driver():
    URLList = []
    for URL in URL_FILE:
        busScore = busFactor()
        correct = 0
        responsive = 0
        rampUp = 0
        licenseScore = 0
        net_score = sum(busScore, correct, responsive, rampUp, licenseScore) / 5
        URLList.append({URL:{TotalScore: net_score, License: licenseScore, RampUp: rampUp, BusFactor: busScore, ResponsiveMaintainers: responsive, Correct: correct}})
    with open("output.NDJSON", "w") as out:
        ndjson.dumps(URLList,out)
    out.close()    

def license_func(owner_repo, git_token):
    
    # Get list of possible licenses from Github
    licenseList = licenseScore.getLicensesList(git_token)
    
    licenseName = licenseScore.githubLicense(owner_repo, git_token, licenseList)

    # Assigns a score according to the license
    scoreLicense = licenseScore.score(licenseList, licenseName)
    return scoreLicense, licenseName
 
def parser_driver():
    url = sys.argv[1]
    
    # Parse the URL to get to the absolute Webpage name
    url_domain = urlparse(url).netloc.split('.')
    
    # Gets Github Repo from NPM API
    if("npmjs" in url_domain):
        url = licenseScore.npm_to_git(url)
    
    # Get Repo Name, Owner and Git Token    
    owner_repo, git_token = licenseScore.get_owner_repo(url)

    # Get Scores for all URL Categories
    license_score, licenseName = license_func(owner_repo, git_token)
    #correctness_score, correctnessList = correctness_func(owner_repo, git_token)
    
    # Outputs the Scores in JSON Format
    jsonDict = {}
    for categories in ["license_score"]:
        jsonDict[categories] = eval(categories)

    print(license_score, licenseName)
    #print("Correctness Scores: ", correctnessList)
    print(json.dumps(jsonDict))
    return 0
    
if __name__ == "__main__":
    #main_driver()
    parser_driver()
    #print("Hello World")

