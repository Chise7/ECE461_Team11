import github as Github
from RampUp import npm_to_git_rep
import ctypes
rustLib = ctypes.CDLL("Run/target/debug/rustlib.dll")

def busFactor():
    URL = "https://github.com/Chise7/ECE461_Team11"
    g = Github() #figure out how to provide gittokens :( <- GITTOKEN HERE?
    repo = g.get_repo(URL)
    commits = repo.get_commits()
    authors = []
    for commit in commits:
        if commit.author.name not in authors: authors.append(commit.author.name)
        print(commit.author.name)
    numOfAuthors = len(authors)
    busFunc = rustLib.bus_score
    return(busFunc(numOfAuthors))