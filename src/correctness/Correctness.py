import requests
import ctypes   # Future Use

def get_downloads(owner_repo, git_token):
    api_Url = f"https://api.github.com/repos/{owner_repo}/releases"
    headers = {"Authorization": f"{git_token}"}
    downloads_request = requests.get(api_Url, headers=headers)
    releases = downloads_request.json()
    downloads_score = 0
    release_count = len(releases)
    if(downloads_request.status_code == 200):
        try: # Try to see if it exists
            if("download_count" in releases[0]["assets"][0]): 
                for version in range(0, release_count - 1):
                    downloads_score += int(releases[version]["assets"][0]["download_count"])
                if(downloads_score > 1000):
                    downloads_score = 0.15
                else:
                    downloads_score = 0
        except:
            downloads_score = 0

    else:
        downloads_score = 0

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
    # Base API Call for Total Issues Open and Closed
    api_Url_open = f"https://api.github.com/search/issues?q=repo:{owner_repo}%20is:issue%20is:open&per_page=1"
    api_Url_closed = f"https://api.github.com/search/issues?q=repo:{owner_repo}%20is:issue%20is:closed&per_page=1"
    headers = {"Authorization": f"{git_token}"}
    
    # Get both Open and Closed Issues Count
    open_issues_request = requests.get(api_Url_open, headers=headers)
    closed_issues_request = requests.get(api_Url_closed, headers=headers)
    
    if(closed_issues_request.status_code == 200 and open_issues_request.status_code == 200):
        total_count = int(open_issues_request.json()["total_count"]) + int(closed_issues_request.json()["total_count"])
        if(total_count > 100):
            issues_score = 0.15
        else:
            issues_score = 0
    else:
        issues_score = 0
    
    return issues_score

def get_pr(owner_repo, git_token): 
    # Base API Call for Total Pull Requests Open and Closed
    api_Url_open = f"https://api.github.com/search/issues?q=repo:{owner_repo}%20is:pr%20is:open&per_page=1"
    api_Url_closed = f"https://api.github.com/search/issues?q=repo:{owner_repo}%20is:pr%20is:closed&per_page=1"
    headers = {"Authorization": f"{git_token}"}
    
    # Get both Open and Closed Issues Count
    open_pr_request = requests.get(api_Url_open, headers=headers)
    closed_pr_request = requests.get(api_Url_closed, headers=headers)
    
    if(open_pr_request.status_code == 200 and closed_pr_request.status_code == 200):
        total_count = int(open_pr_request.json()["total_count"]) + int(closed_pr_request.json()["total_count"])
        if(total_count > 50):
            pr_score = 0.15
        else:
            pr_score = 0
    else:
        pr_score = 0
    
    return pr_score

def get_Resp_Maintainer():  # This code can maybe be done in Rust
    maintainer_score = 1 # This will be passed as an arguement depending on the Resp Maintainer Code
    rm_percent = 0.30
    rm_score = maintainer_score * rm_percent
    rm_score = 0

    return rm_score