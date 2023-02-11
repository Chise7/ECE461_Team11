import re
import sys
import requests
from github import Github

def url_checker(url):
    # regex for a proper repository URL structure
    pattern = re.compile(r"(https:\/\/)?(www.)?([A-z]+\.[A-z]+\/[\w-]+\/[\w-]+)")
    if not re.fullmatch(pattern, url): return "Invalid URL!"
    else: return "Valid URL!"

def npm_to_git_rep(npmDirectory):
    url = f"https://registry.npmjs.org/{npmDirectory}"
    getGit = requests.get(url)
    if getGit.status_code == 200:
        if 'repository' in getGit.json() or 'url' in getGit.json():
            gitURL = getGit.json()['repository']['url']
            if "github" in gitURL:
                result = re.search(r"/([\w-]+)/([\w-]+)", gitURL.lower())
                git_owner = ""
                if result is not None:
                    git_owner = result[1]
                else: git_owner = "guh"
                return git_owner
    return "guh"

def ramp_up(url, persToken):
    # Check if valid repo URL
    checked = url_checker(url)
    if checked == "Invalid URL!": return -1
    # Extract repo directory
    gitPattern = re.compile(r"\/[\w-]+\/[\w-]+")
    unver = gitPattern.search(url)
    if unver == None: return -2
    unverDir = unver.group(0)[1:]
    # Check Git vs NPM URLS
    # Cross-compatibility here relies entirely on if the repo has a Github entry
    repoDir = ""
    if "npmjs.com" in url:
        # print("valid NPM git repo format")
        unverDir = unverDir.replace("package/", "")
        repoDir = npm_to_git_rep(unverDir)
        if "guh" in repoDir: return -3
    elif "github.com" in url:
        # print("valid Github repo format")
        if requests.get(url).status_code != 200: return -4
        repoDir = unverDir
    else:
        return -5
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
        if "README" in objects.name or "readme" in objects.name:
            # print("README Found")
            readFound = True
    # Scoring from overall metrics
    if folderCount < 10:
        folderWeight *= 1
    elif folderCount < 16:
        folderWeight *= 0.5
    elif folderCount >= 16:
        folderWeight *= 0
    if not readFound: readWeight = 0
    totalScore = int((folderWeight + readWeight) * 100)
    return totalScore


if __name__ == '__main__':
    score = ramp_up(sys.argv[1], sys.argv[2])
    print(score)