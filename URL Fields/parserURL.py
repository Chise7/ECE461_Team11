from urllib.parse import urlparse
from License import licenseScore
from Correctness import correctnessScore
import sys
import json

def license_func(owner_repo, git_token):
    
    # Get list of possible licenses from Github
    licenseList = licenseScore.getLicensesList(git_token)
    
    licenseName = licenseScore.githubLicense(owner_repo, git_token, licenseList)

    # Assigns a score according to the license
    scoreLicense = licenseScore.score(licenseList, licenseName)
    return scoreLicense, licenseName

def correctness_func(owner_repo, git_token):
    
    correcntessList = [
        correctnessScore.get_Resp_Maintainer(),
        correctnessScore.get_downloads(owner_repo, git_token), 
        correctnessScore.get_downloads(owner_repo, git_token),    
        correctnessScore.get_doc(owner_repo, git_token),
        correctnessScore.get_stars(owner_repo, git_token),
        correctnessScore.get_issues(owner_repo, git_token),
        correctnessScore.get_pr(owner_repo, git_token)]
    
    return sum(correcntessList)

if __name__ == "__main__":
    
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
    correctness_score = correctness_func(owner_repo, git_token)
    
    # Outputs the Scores in JSON Format
    jsonDict = {}
    for categories in ["license_score","correctness_score"]:
        jsonDict[categories] = eval(categories)

    #result = licenseScore.rustScore()
    #print(result)
    #print(licenseName)
    print(json.dumps(jsonDict))