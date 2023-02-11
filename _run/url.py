from urllib.parse import urlparse
from license import license
from correctness import correctness
from bus_factor import bus_factor
import sys
import ndjson
import os
import ctypes
import json
rustLib = ctypes.CDLL("rustlib/target/debug/rust_lib.dll")
netFunc = rustLib.net_score

def main_driver():
    token = os.getenv('GITHUB_TOKEN')
    URLList = []
    URL_FILE = open(sys.argv[1])
    urlLines = URL_FILE.readlines()
    
    for URL in urlLines:
        URL = URL.split("\n")[0]
        # Parse the URL to get to the absolute Webpage name
        url_domain = urlparse(URL).netloc.split('.')
        
        # Gets Github Repo from NPM API
        if("npmjs" in url_domain):
            URL = license.npm_to_git(URL)

    
        # Get Repo Name and Owner    
        owner_repo = license.get_owner_repo(URL)

        responsive = 0
        #busScore = bus_factor.busFactor(URL,token)
        correctness_score = correctness_func(owner_repo, token, URL)
        rampUp = 0
        license_score = license_func(owner_repo, token, rustLib)
        #net_score = netFunc(busScore,correctness_score,responsive,rampUp,license_score)#sum(busScore, correct, responsive, rampUp, licenseScore) / 5
        #URLList.append({URL:{"TotalScore": net_score, "License": license_score, "RampUp": rampUp, "BusFactor": busScore, "ResponsiveMaintainers": responsive, "Correct": correctness_score}})

        jsonDict = {}
        for categories in ["license_score", "correctness_score"]:
            jsonDict[categories] = eval(categories)

        print(json.dumps(jsonDict))
    return 0
    #with open("output.NDJSON", "w") as out:
    #    ndjson.dumps(URLList,out)
    #out.close()    

def license_func(owner_repo, git_token, rustLib):
    
    # Get list of possible licenses from Github
    licenseList = license.getLicensesList(git_token)
    
    licenseName = license.githubLicense(owner_repo, git_token, licenseList)
    
    # Assigns a score according to the license
    scoreLicense = license.rust_Score(licenseName, licenseList, rustLib)
    print(licenseName)
    return scoreLicense
 
def correctness_func(owner_repo, git_token, url):
    
    correcntessList = [
        #correctnessScore.get_Resp_Maintainer(),   # Still needs Resp Maintainer Score
        correctness.get_tags(url),
        correctness.get_downloads(owner_repo, git_token),    
        correctness.get_doc(owner_repo, git_token),
        correctness.get_stars(owner_repo, git_token),
        correctness.get_issues(owner_repo, git_token),
        correctness.get_pr(owner_repo, git_token)]
    print(correcntessList)
    return sum(correcntessList)
    
if __name__ == "__main__":
    main_driver()
    #license.npm_to_git("https://www.npmjs.com/package/even")