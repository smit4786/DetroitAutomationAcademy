import asyncio
import httpx
import sys
import os

# Add parent directory to path to allow importing from utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import get_repo_info, GitHubDeps

async def main():
    """
    Example of how to use the get_repo_info function.
    """
    deps = GitHubDeps()
    deps.client = httpx.AsyncClient()
    # No GitHub token is provided, so the rate limit will be lower.
    # For higher rate limits, you can set deps.github_token = "YOUR_TOKEN"
    deps.github_token = None

    repo_url = "https://github.com/smit4786/DetroitAutomationAcademy"
    repo_info = await get_repo_info(deps, repo_url)
    print(repo_info)

    await deps.client.aclose()

if __name__ == "__main__":
    asyncio.run(main())