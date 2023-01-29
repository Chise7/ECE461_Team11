import re
import sys
import requests
from github import Github

persToken = "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"

def url_checker(url):
    # regex for a proper repository URL structure
    pattern = re.compile(r"(https:\/\/)?(www.)?([A-z]+\.[A-z]+\/[\w-]+\/[\w-]+)")
    if not re.fullmatch(pattern, url):
        return "Invalid URL!"
    else:
        return "Valid URL!"


def npm_to_git_rep(npmDirectory):
    urlAcq = f"https://registry.npmjs.org/{npmDirectory}"
    getGit = requests.get(urlAcq)
    if getGit.status_code == 200:
        gitURL = getGit.json()['repository']['url']
        if "github" in gitURL:
            gitPattern = re.compile(r"\/[A-z]+\/[A-z]+")
            gitStripped= gitPattern.search(gitURL)
            gitURL = gitStripped.group(0)[1:]
            return gitURL
        else:
            return "Non-Github URL"

    else:
        return "NPM Error"

def ramp_up(url):
    # Check if valid repo URL
    checked = url_checker(url)
    if checked == "Invalid URL!":
        return checked
    # Extract repo directory
    gitPattern = re.compile(r"\/[A-z]+\/[A-z]+")
    unver = gitPattern.search(url)
    unverDir = unver.group(0)[1:]
    # Check Git vs NPM URLS
    # Cross-compatibility here relies entirely on if the repo has a Github entry
    repoDir = ""
    if "npmjs.com" in url:
        #print("valid NPM git repo format")
        unverDir = unverDir.replace("package/","")
        repoDir = npm_to_git_rep(unverDir)
    elif "github.com" in url:
        #print("valid Github repo format")
        repoDir = unverDir
    else:
        return "Not a compatible URL!"

    # Evaluating Github Repository contents
    folderCount = 0
    folderWeight = 0.75
    readWeight = (1 - folderWeight)
    readFound = False
    g = Github(persToken)
    gitRepo = g.get_repo(repoDir)
    rootDir = gitRepo.get_contents("")

    # Loop through root contents to check for folders
    for objects in rootDir:
        if objects.type == "dir":
            folderCount += 1
        if "README" in objects.name:
            #print("README Found")
            readFound = True

    # Scoring from overall metrics
    if folderCount < 10:
        folderWeight *= 1
    elif folderCount < 16:
        folderWeight *= 0.5
    elif folderCount >= 16:
        folderWeight *= 0

    if not readFound:
        readWeight = 0

    totalScore = folderWeight + readWeight
    return totalScore
if __name__ == '__main__':
    score = ramp_up(sys.argv[1])
    if(type(score) is str):
        print("Error Encountered")
    print(score)