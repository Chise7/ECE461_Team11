from github import Github
import subprocess
import ctypes
rustLib = ctypes.cdll.LoadLibrary("Run/target/release")

def main_driver():
    busScore = busFactor()

def busFactor():
    g = Github(gitToken) #figure out how to provide gittokens :(
    repo = g.get_user().get_repo("ECE461_Team11")
    commits = repo.get_commits()
    authors = []
    for commit in commits:
        if commit.author.name not in authors: authors.append(commit.author.name)
    numOfAuthors = len(authors)
    rustLib.get_result("test")
    return(0)

if __name__ == "__main__":
    main_driver()

