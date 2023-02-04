from urllib.parse import urlparse
from License import licenseScore
from Correctness import correctnessScore
import sys
import json


url = sys.argv[1]

# Parse the URL to get to the absolute Webpage name
url_split = urlparse(url).netloc.split('.')

# Get list of possible licenses from Github
licenseList = licenseScore.getLicensesList()

# Calls Function for different API calls according to URL Domain
if("github" in url_split):
    licenseName = licenseScore.githubLicense(url, licenseList)
elif("npmjs" in url_split):
    git_url = licenseScore.npm_to_git(url)
    licenseName = licenseScore.githubLicense(git_url, licenseList)
 
# Assigns a score according to the license
scoreLicense = licenseScore.score(licenseList, licenseName)
scoreCorrect = 0

# Outputs the Score in JSON Format
jsonDict = {}
for categories in ["scoreCorrect","scoreLicense"]:
    jsonDict[categories] = eval(categories)

result = licenseScore.rustScore()
print(result)
print(licenseName)
print(json.dumps(jsonDict))