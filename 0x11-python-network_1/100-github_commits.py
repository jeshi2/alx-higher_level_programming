#!/usr/bin/python3
"""
Python script that takes 2 arguments in
order to solve this challenge.
"""
import requests
import sys


def list_commits(owner, repo):
    """
    Lists 10 most recent commits of a repository by a user
    """
    base_url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    params = {'per_page': 10}
    headers = {'Accept': 'application/vnd.github.v3+json'}

    try:
        response = requests.get(base_url, params=params, headers=headers)

        if response.status_code == 200:
            commits = response.json()
            for commit in commits:
                sha = commit['sha']
                author_name = commit['commit']['author']['name']
                print(f"{sha}: {author_name}")
        else:
            print(f"Error: {response.status_code}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: python3 100 - github_commits.py "
              f"< repository_name > <owner_name >"
              )
        sys.exit(1)

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    list_commits(owner_name, repo_name)
