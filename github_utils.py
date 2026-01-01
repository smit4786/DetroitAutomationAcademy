import httpx
import re
from typing import Optional
from pydantic import BaseModel, Field

class GitHubConfig(BaseModel):
    """GitHub API configuration.

    This model defines the configuration for the GitHub API, including
    the optional token for authentication and the API URL.
    """

    token: Optional[str] = Field(None, description='GitHub API token for increased rate limits')
    api_url: str = Field(
        default='https://api.github.com/graphql', description='GitHub GraphQL API URL'
    )

class GitHubDeps:
    client: httpx.AsyncClient
    github_token: str | None = None

async def get_repo_info(deps: GitHubDeps, github_url: str) -> str:
    """Get repository information including size and description using GitHub API.

    Args:
        deps: The dependencies.
        github_url: The GitHub repository URL.

    Returns:
        str: Repository information as a formatted string.
    """
    match = re.search(r'github\.com[:/]([^/]+)/([^/]+?)(?:\.git)?$', github_url)
    if not match:
        return "Invalid GitHub URL format"

    owner, repo = match.groups()
    headers = {'Authorization': f'token {deps.github_token}'} if deps.github_token else {}

    response = await deps.client.get(
        f'https://api.github.com/repos/{owner}/{repo}',
        headers=headers
    )

    if response.status_code != 200:
        return f"Failed to get repository info: {response.text}"

    data = response.json()
    size_mb = data['size'] / 1024

    return (
        f"Repository: {data['full_name']}\n"
        f"Description: {data['description']}\n"
        f"Size: {size_mb:.1f}MB\n"
        f"Stars: {data['stargazers_count']}\n"
        f"Language: {data['language']}\n"
        f"Created: {data['created_at']}\n"
        f"Last Updated: {data['updated_at']}"
    )
