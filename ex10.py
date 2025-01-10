
# EXERCISE 10: Working with REST APIs

# Write a program that:
# connects to GitHub API
# gets all the public repositories for a specific GitHub user
# prints the name & URL of every project

import requests


github_username = 'susott'
response = requests.get(f"https://api.github.com/users/{github_username}/repos")

repositories = response.json()

for repo in repositories:
    print(f"{repo['name']} - {repo['url']}")
