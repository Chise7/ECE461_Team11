import requests
import base64
import ctypes

def get_downloads(owner_repo, git_token):
    api_Url = f"https://api.github.com/repos/{owner_repo}/releases"
    headers = {"Authorization": f"{git_token}"}
    downloads_request = requests.get(api_Url, headers=headers)
    releases = downloads_request.json()
    downloads_score = 0

    
    if(downloads_request.status_code == 200):
        #for version in releases:
        print(releases[1]["assets"])
            #break
            #downloads_score += version["download_count"]
        
        #downloads_score = 0.15

    #     downloads_score = 0.15
    return downloads_score

def get_doc(owner_repo, git_token):
    api_Url = f"https://api.github.com/repos/{owner_repo}/readme"
    headers = {"Authorization": f"{git_token}"}
    get_readme = requests.get(api_Url, headers=headers)
    if(get_readme.status_code == 200):
        doc_score = 0.20
    else:
        doc_score = 0

    return doc_score


def get_stars(owner_repo, git_token):
    api_Url = f"https://api.github.com/repos/{owner_repo}"
    headers = {"Authorization": f"{git_token}"}
    star_request = requests.get(api_Url, headers=headers)
    
    if(star_request.status_code == 200):
        star_count = int(star_request.json()["stargazers_count"])
        if(star_count > 1000):
            stars_score = 0.05
        else:
            stars_score = 0
    else:
        stars_score = 0

    return stars_score

def get_issues(owner_repo, git_token):
    
    issues_score = 0

    #issues_score = 0.15
    return issues_score

def get_pr(owner_repo, git_token): 
    
    # pr_score = 0.15
    pr_score = 0
    return pr_score

def get_Resp_Maintainer():
    #rm_score = 0.30
    rm_score = 0

    return rm_score

# Correctness Metrics
# Number of Downloads
# Number of Starts
# Number of Issues
# Number of Pull Requests


# Correctness Score Formula
#   Documentation                       0.20
#   Number of Downloads exceeds 1000    0.15
#   Number of Stars                     0.05    
#   Number Solved and Unsolved Issues   0.15
#   Number of Pull Requests             0.15
#                                     = 0.70

# RespMaintainer                      = 0.30
# Total                                 1.00