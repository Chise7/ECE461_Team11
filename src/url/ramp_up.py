import sys
import requests
from github import Github

def ramp_up(owner, repo, token):

    repoDir = f"{owner}/{repo}"

    # Evaluating Github Repository contents
    folderCount = 0
    folderWeight = 0.75
    readWeight = (1 - folderWeight)
    readFound = False
    g = Github(token)
    checky = requests.get("https://github.com/"+repoDir)
    if checky.status_code != 200: return -1
    gitRepo = g.get_repo(repoDir)
    rootDir = gitRepo.get_contents("")

    # Loop through root contents to check for folders
    for objects in rootDir:
        if objects.type == "dir":
            folderCount += 1
        if "README" in objects.name or "readme" in objects.name:
            #print("README Found")
            readFound = True

    # Scoring from overall metrics
    if folderCount <= 7:
        folderWeight *= 1
    elif folderCount < 10:
        folderWeight *= 0.5
    elif folderCount >= 15:
        folderWeight *= 0

    if not readFound:
        readWeight = 0

    totalScore = int((folderWeight + readWeight) * 100)
    return float(totalScore) / 100

if __name__ == '__main__': # pragma: no cover
    ramp_up_score = ramp_up(sys.argv[1], sys.argv[2], sys.argv[3])
    print(ramp_up_score, end="")