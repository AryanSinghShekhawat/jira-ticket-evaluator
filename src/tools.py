import os
import requests
from langchain_core.tools import tool
from dotenv import load_dotenv
from typing import Dict, Any

load_dotenv()

@tool
def fetch_jira_ticket(ticket_key: str) -> Dict[str, Any]:
    """Fetch Jira ticket details."""
    url = f"{os.getenv('JIRA_BASE_URL')}/rest/api/3/issue/{ticket_key}"
    auth = (os.getenv('JIRA_EMAIL'), os.getenv('JIRA_API_TOKEN'))
    resp = requests.get(url, auth=auth)
    return resp.json()

@tool
def fetch_pr_diff(pr_url: str) -> Dict[str, Any]:
    """Fetch GitHub PR diff and files."""
    parts = pr_url.split('/')
    owner, repo, pr_num = parts[-4], parts[-3], parts[-1]
    headers = {"Authorization": f"token {os.getenv('GITHUB_TOKEN')}"}
    
    pr_url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_num}"
    files_url = f"{pr_url}/files"
    
    pr = requests.get(pr_url, headers=headers).json()
    files = requests.get(files_url, headers=headers).json()
    return {"pr": pr, "files": files}
