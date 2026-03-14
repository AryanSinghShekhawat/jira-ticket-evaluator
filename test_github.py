import requests
import os
from dotenv import load_dotenv
load_dotenv()

headers = {"Authorization": f"token {os.getenv('GITHUB_TOKEN')}"}
response = requests.get("https://api.github.com/user", headers=headers)
print("✅ GitHub Ready!" if response.status_code == 200 else "❌ Token failed")
