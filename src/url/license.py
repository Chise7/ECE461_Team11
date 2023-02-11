import sys
import requests
import base64
import ctypes

def get_owner_repo(url):
    ownerRepo = url.replace("https://github.com/", "") # get the owner and repo name separated for api call
    ownerRepo = ownerRepo.replace(".git", "")
    return ownerRepo

# Request to get Github Repo License
def githubLicense(owner, repo, token, licenseList):
    api_Url = f"https://api.github.com/repos/{owner}/{repo}/license"
    headers = {"Authorization": f"{token}"}
    get_license = requests.get(api_Url, headers=headers)
    
    # Checks if the API call was successful for the License File
    if(get_license.status_code != 200):
        readmeLicense = searchReadme(api_Url, headers, token)
        licenseName = "License Error"
        if(readmeLicense != "No License"):
            licenseName = readmeLicense
        return licenseName
    else:
        licenseName = get_license.json()["license"]["name"]
        # Second way of checking for license if there was a Null Name for License
        if(licenseName not in licenseList):
            readmeLicense = searchReadme(api_Url, headers, token)
            if(readmeLicense != "No License"):
                licenseName = readmeLicense
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
    
# Gets Github lists of Approved Licenses with LGPL v2.1
def getLicensesList(git_token):
    licenseNames = []
    licenses_url = f"https://api.github.com/licenses"
    headers = {"Authorization": f"{git_token}"}
    licenseList = requests.get(licenses_url, headers=headers)
    if(licenseList.status_code == 200):
        licenseList = licenseList.json()
        licenseNames = approved_licenses(licenseList,licenses_url, headers)
        return licenseNames
    else:
        return "Error"

def approved_licenses(licenseList, api_url, headers):
    new_list = ["GNU Lesser General Public License v2.1"]  # Original License to Account
    copyleft = []
    for license in licenseList:
        url = api_url + "/" + license["key"]
        licenseList = requests.get(url, headers=headers)
        if(licenseList.status_code == 200):
            licenseList = licenseList.json()
            description = licenseList['description']
            if("permissive" in description):
                new_list.append(license["name"])
            elif("no conditions" in description):
                new_list.append(license["name"])
            if("GNU Lesser General Public License v2.1" or "LGPL v2.1" in licenseList['body']):
                copyleft.append(license["name"])
        else:
            print("API Error")
    return new_list

# Searches for any License mentioned in the README
def searchReadme(url, headers, git_token):
    url = url.rsplit("/", 1)[0] + "/readme"
    getReadme = requests.get(url, headers=headers)
    if(getReadme.status_code != 200):
        return "No License"
    else:
        readmeContent = getReadme.json()["content"].encode("utf-8")
        readmeContent = base64.b64decode(readmeContent)
        readmeContent = str(readmeContent).lower()
        licenseList = getLicensesList(git_token)
        licenseList = [i.lower() for i in licenseList]

        for gitLicense in licenseList:
            if gitLicense in readmeContent:
                return gitLicense
        return "No License"   

def rust_score(owner, repo, token):
    license_list = getLicensesList(token)
    
    license_name = githubLicense(owner, repo, token, license_list).lower()

    license_list = ", ".join(license_list).lower()    
    # rust_lib = ctypes.CDLL('target/debug/rustlib.dll')
    
    # Call Rust Function with license name in binary
    if license_name in license_list:
        return 1.0
    else:
        return 0.0

if __name__ == "__main__":
    # license_score = 1.0
    license_score = rust_score(sys.argv[1], sys.argv[2], sys.argv[3])
    print(license_score, end="")