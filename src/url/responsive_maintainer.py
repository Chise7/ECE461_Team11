import sys
# import requests
from github import Github, Repository

GITHUB_API_URL = 'https://api.github.com'

def get_weekly_subscore(git_repo: Repository.Repository) -> float:
    # while True:

    #     response = session.get(
    #         url=GITHUB_API_URL+f'/repos/{owner}/{repo}/stats/code_frequency',
    #         # headers={
    #         #     'If-None-Match': 'cea248d061577674615529d3713a77b7c2b5ef361ee9406088b54584da93fdfe'
    #         # }
    #     )

    #     if len(response.json()) > 0:
    #         break
    # response = git_repo.get_stats_code_frequency()

    # weekly_additions = 0.0
    # weekly_deletions = 0.0

    # if response is not None:
    #     print(response)
    #     week, weekly_additions, weekly_deletions = response 
    #     if weekly_additions is not None:
    #         weekly_additions = 0.0
    #     if weekly_deletions is not None:
    #         weekly_deletions = 0.0

    # if response.status_code != 200 and response.status_code != 202 and response.status_code != 204:
    #     return -1.0

    # weekly_additions = 0
    # weekly_deletions = 0
    # for item in response.json():
    #     weekly_additions += item[1]
    #     weekly_deletions += item[2]

    # weekly_adds_and_dels = float(weekly_additions - weekly_deletions)
    # if weekly_adds_and_dels > 10000000:
    #     return 1.0
    # elif weekly_adds_and_dels > 1000000:
    #     return 0.75
    # elif weekly_adds_and_dels > 100000:
    #     return 0.5
    # elif weekly_adds_and_dels > 10000:
    #     return 0.25
    # else:
    #     return 0.0
    
    return 0.0


def get_yearly_subscore(git_repo: Repository.Repository) -> float:
    response = git_repo.get_stats_commit_activity()
    yearly_commits = 0
    if response is not None:
        for commit_activity in response:
            if commit_activity is not None:
                yearly_commits += int(commit_activity.total)

    if yearly_commits > 1000:
        return 1.0
    elif yearly_commits > 500:
        return 0.75
    elif yearly_commits > 100:
        return 0.5
    elif yearly_commits > 10:
        return 0.25
    else:
        return 0.0


def get_rm_score(owner: str, repo: str, token: str) -> float:
    # owner, repo = parse_url(url)
    g = Github(token)
    git_repo = g.get_repo(f"{owner}/{repo}")

    # session = requests.Session()
    # session.auth = (token)

    yearly_subscore = get_yearly_subscore(git_repo)
    weekly_subscore = get_weekly_subscore(git_repo)

    rm_score = \
        0.75 * yearly_subscore + \
        0.25 * weekly_subscore

    return rm_score

if __name__ == "__main__":
    # responsive_maintainer_score = 0.64
    rm_score = get_rm_score(sys.argv[1], sys.argv[2], sys.argv[3])
    print(rm_score, end="")