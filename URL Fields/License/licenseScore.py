import requests

# Request to get Github Repo License
def githubLicense(ownerRepo):
    ownerRepo = ownerRepo.replace("https://github.com/", "") # get the owner and repo name separated for api call
    ownerRepo = ownerRepo.replace(".git", "")
    gitToken = "" # ADD HERE YOUR GITHUB TOKEN
    url_arg = f"https://api.github.com/repos/{ownerRepo}/license"
    headers = {'Authorization': f'{gitToken}'}
    get_license = requests.get(url_arg, headers=headers)
    
    # Checks if the API call was successful
    if(get_license.status_code != 200):
        print("Error! Github")
        return "Error"
    else:
        licenseName = get_license.json()['license']['name']
        return licenseName

# NPM Package will get Github Repo from it's registry and use Github API to get License
def npmLicense(packageName):
    packageName = packageName.replace("https://www.npmjs.com/package/", "") # get the package name separated for api call
    url_arg2 = f"https://registry.npmjs.org/{packageName}"
    get_license2 = requests.get(url_arg2)
    if(get_license2.status_code != 200):
        print("Error! NPM")
        return "Error"
    else:
        licenseName2 = get_license2.json()['repository']['url']
        
        # NPM packages may also use different repositories such as Bitbucket
        if("github" in licenseName2):
            licenseName2 = licenseName2.replace("git:","https:")
            return githubLicense(licenseName2)
        else:
            return "Not a Github Repository!"
    
# Gets Github lists of Licenses
def getLicensesList():
    licenseNames = []
    gitToken = "" # ADD HERE YOUR GITHUB TOKEN
    licenses_url = f"https://api.github.com/licenses"
    headers = {'Authorization': f'{gitToken}'}
    licenseList = requests.get(licenses_url, headers=headers).json()
    for i in licenseList:
        licenseNames.append(i['name'])
    return licenseNames

if __name__ == '__main__':
    print()

# License Scoring System for Modules and Packages for Github and NPM
    # Software packages will receive a score of 0 if it includes no license whatsoever in any of their files (license file and or README)
    # Software packages will receive a score of 0.25 if it includes a license, but is not a GNU Lesser General Public License of any version
    # Softwar packages will receive a score of 0.50 if the license is a GNU LGPL of any version but v2.1
    # Software packages will receive a score of 1 if the license is GNU LGPL v2.1 as required by ACME

def score(licenseList, licenseName):
    score = 0
    if(licenseName in licenseList):
        score = 0.25
    if("GNU" in licenseName):
        score = 0.5
    if("v2.1" in licenseName):
        score  = 1
    return score