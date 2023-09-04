#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to
solve hoberton challenge
"""
import requests
import sys


def list_commits(owner, repo, count=10):
    """
    Lists recent commits from a GitHub
    repository by the specified owner
    """
    try:
        url = (
            f"https://api.github.com/repos/{owner}/{repo}/"
            f"commits?per_page={count}"
        )
        response = requests.get(url)

        if response.status_code == 200:
            commits = response.json()
            sorted_commits = sorted(
                commits,
                key=lambda x: x['commit']['author']['date'],
                reverse=True)
            for commit in sorted_commits:
                sha = commit['sha']
                author_name = commit['commit']['author']['name']
                print(f"{sha}: {author_name}")
        else:
            print(
                f"Error: Unable to fetch commits "
                f"(HTTP {response.status_code})"
            )
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 100-github_commits.py <owner> <repo>")
        sys.exit(1)

    owner = sys.argv[1]
    repo = sys.argv[2]

    list_commits(owner, repo)
