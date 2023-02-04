import requests
import base64
import ctypes

def get_owner_repo(url):
    ownerRepo = url.replace("https://github.com/", "") # get the owner and repo name separated for api call
    ownerRepo = ownerRepo.replace(".git", "")
    gitToken = "" # ADD HERE YOUR GITHUB TOKEN
    return ownerRepo, gitToken

# Request to get Github Repo License
def githubLicense(owner_repo, git_token, licenseList):
    api_Url = f"https://api.github.com/repos/{owner_repo}/license"
    headers = {"Authorization": f"{git_token}"}
    get_license = requests.get(api_Url, headers=headers)
    
    # Checks if the API call was successful for the License File
    if(get_license.status_code != 200):
        licenseName = searchReadme(api_Url, headers)
        return licenseName
    else:
        licenseName = get_license.json()["license"]["name"]
        # Second way of checking for license if there was a Null Name for License
        if(licenseName not in licenseList):
            licenseName = searchReadme(api_Url, headers)
        return licenseName

# NPM API will get Github Repo from it's registry
def npm_to_git(npm_url):
    npm_url = npm_url.replace("https://www.npmjs.com/package/", "") # get the package name separated for api call
    api_Url = f"https://registry.npmjs.org/{npm_url}"
    get_license2 = requests.get(api_Url)
    
    if(get_license2.status_code != 200):
        print("Error! NPM")
        return "Error"
    else:
        repo_url = get_license2.json()["repository"]["url"]
        # NPM packages may also use different repositories such as Bitbucket
        if("github" in repo_url):
            # Replace all words before github keyword
            urlIndex = repo_url.index("github")
            repo_url = "https://" + repo_url[urlIndex:]
            return repo_url
        else:
            return "Not a Github Repository!"
    
# Gets Github lists of Licenses
def getLicensesList(git_token):
    licenseNames = []
    licenses_url = f"https://api.github.com/licenses"
    headers = {"Authorization": f"{git_token}"}
    licenseList = requests.get(licenses_url, headers=headers)
    if(licenseList.status_code == 200):
        licenseList = licenseList.json()
        for i in licenseList:
            licenseNames.append(i["name"])
        return licenseNames
    else:
        print(licenseList.status_code)
        return "Error"

# Searches for any License mentioned in the README
def searchReadme(url, headers):
    url = url.rsplit("/", 1)[0] + "/readme"
    getReadme = requests.get(url, headers=headers)
    if(getReadme.status_code != 200):
        return "No Readme"
    else:
        readmeContent = getReadme.json()["content"].encode("utf-8")
        readmeContent = base64.b64decode(readmeContent)
        readmeContent = str(readmeContent).lower()
        licenseList = getLicensesList()
        licenseList = [i.lower() for i in licenseList]

        for gitLicense in licenseList:
            if gitLicense in readmeContent:
                return gitLicense
        return "No License in Readme"   

def rustScore():
    rust_lib = ctypes.CDLL('License/license_score/target/debug/rustypython.dll')

    rust_function = rust_lib.get_string
    score_function = rust_lib.get_score
    rust_function.restype = ctypes.c_char_p
    score_function.restype = ctypes.c_double
    resultString = rust_function().decode()
    scoreDouble = score_function().decode()
    print(scoreDouble)
    return resultString

def score(licenseList, licenseName):
    licenseList = [i.lower() for i in licenseList]
    licenseName = licenseName.lower()
    #return 0 #rustScore(licenseList, licenseName)
    score = 0
    
    if("v2.1" in licenseName):
        score  = 1
    elif("GNU" in licenseName):
        score = 0.5
    elif(licenseName in licenseList):
        score = 0.25
    return score