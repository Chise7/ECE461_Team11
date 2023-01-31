# To run the license files use this command with a github or npm link like this one:
# Don't forget to add your Github Token on the licenseScore file
# python parserURL.py https://github.com/jonschlinkert/even

from urllib.parse import urlparse
from License import licenseScore
import sys
import json
#import subprocess

url = sys.argv[1]

# Parse the URL to get to the absolute Webpage name
url_split = urlparse(url).netloc.split('.')

# Calls Function for different API calls according to URL Domain
if("github" in url_split):
    licenseName = licenseScore.githubLicense(url)
elif("npmjs" in url_split):
    licenseName = licenseScore.npmLicense(url)  
 
# Get list of possible licenses from Github
licenseList = licenseScore.getLicensesList()

# Assigns a score according to the license
scoreLicense = licenseScore.score(licenseList, licenseName)

# Outputs the Score in JSON Format
jsonDict = {}
for categories in ["scoreLicense"]:
    jsonDict[categories] = eval(categories)
    
print(licenseName)
print(json.dumps(jsonDict))

# Run a Rust script with the subprocess library and necessary inputs
# Assign the rust script output to output 
#output = subprocess.run(["parser_script.rs", "arg1", "arg2"], capture_output=True)

# Turn Rust output to string (decode)
#print(output.stdout.decode())