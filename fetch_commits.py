import requests

GITHUB_REPO = "Tanver-Ahammed/mss-DevOps"  # Change this to any public repo
GITHUB_API_URL = f"https://api.github.com/repos/{GITHUB_REPO}/commits"

def fetch_commits():
    response = requests.get(GITHUB_API_URL)

    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:  # Fetch the latest 10 commits
            author_name = commit['commit']['author']['name']
            message = commit['commit']['message']
            print(f"Author: {author_name}\nMessage: {message}\n{'-' * 50}")
    else:
        print(f"Failed to fetch commits: {response.status_code}")


if __name__ == "__main__":
    fetch_commits()
