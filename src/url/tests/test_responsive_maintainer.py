import pytest
from url.responsive_maintainer import *

from github import Github
from url.tests.conftest import TOKEN, TEST_CASES


@pytest.mark.weekly
def test_get_weekly_subscore():
    print("\n\ntesting get_weekly_subscore()")

    g = Github(TOKEN)
    for url, owner, repo in TEST_CASES:
        print(f"test case: ({url}, {owner}, {repo})")
        
        git_repo = g.get_repo(f"{owner}/{repo}")
        weekly_subscore = get_weekly_subscore(git_repo)

        assert type(weekly_subscore) == float, print(f"(owner, repo) = {owner}, {repo}")
        assert weekly_subscore >= 0.0, print(f"(owner, repo) = {owner}, {repo}")
        assert weekly_subscore <= 1.0, print(f"(owner, repo) = {owner}, {repo}")


@pytest.mark.yearly
def test_get_yearly_subscore():
    print("\n\ntesting get_yearly_subscore()")

    g = Github(TOKEN)
    for url, owner, repo in TEST_CASES:
        print(f"test case: ({url}, {owner}, {repo})")

        git_repo = g.get_repo(f"{owner}/{repo}")
        yearly_subscore = get_yearly_subscore(git_repo)

        assert type(yearly_subscore) == float, print(f"(owner, repo) = {owner}, {repo}")
        assert yearly_subscore >= 0.0, print(f"(owner, repo) = {owner}, {repo}")
        assert yearly_subscore <= 1.0, print(f"(owner, repo) = {owner}, {repo}")


@pytest.mark.rm_score
def test_get_rm_score():
    print("\n\ntesting get_rm_score()")
    for url, owner, repo in TEST_CASES:
        print(f"test case: ({url}, {owner}, {repo})")

        rm_score = get_rm_score(owner, repo, TOKEN)

        assert type(rm_score) == float, print(f"(owner, repo) = {owner}, {repo}")
        assert rm_score >= 0.0, print(f"(owner, repo) = {owner}, {repo}")
        assert rm_score <= 1.0, print(f"(owner, repo) = {owner}, {repo}")