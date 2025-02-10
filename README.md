# GitHub Commits Fetcher

A simple script to fetch commit messages and author names from a public GitHub repository, Dockerized for easy deployment.

## Features
- Fetches the latest commits from a public repository.
- Dockerized for easy execution in any environment.
- CI/CD pipeline for automated builds and Docker image publishing.

## Setup & Usage

### 1. Run the Script Locally
```bash
docker run -it tanverit16/fetch-commits sh
python fetch_commits.py
