# To run the license files use this command with a github or npm link like this one:
# Don't forget to add your Github Token on the licenseScore file
# python parserURL.py https://github.com/jonschlinkert/even

from urllib.parse import urlparse
from License import licenseScore
import sys
#import subprocess

url = sys.argv[1]
# Test URLS for testing purposes
#url1 = "https://www.npmjs.com/package/even"
#url2 = "https://github.com/jonschlinkert/even"

# Parse the URL to get to the absolute Webpage name
url_split = urlparse(url).netloc.split('.')


# If Parsed URL is from Github, returns Github to License
if("github" in url_split):
    print("Github")
    licenseName = licenseScore.githubLicense(url)
elif("npmjs" in url_split):
    print("NPM")
    licenseName = licenseScore.npmLicense(url)  
 
# Get list of possible licenses
#licenseList = licenseScore.getLicensesList()

# Assigns a score according to the license
#licenseScore.score(licenseList, licenseName)

# Run a Rust script with the subprocess library and necessary inputs
# Assign the rust script output to output 
#output = subprocess.run(["parser_script.rs", "arg1", "arg2"], capture_output=True)

# Turn Rust output to string (decode)
#print(output.stdout.decode())