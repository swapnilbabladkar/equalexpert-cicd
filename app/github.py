import httpx

GITHUB_API = "https://api.github.com"

async def fetch_public_gists(username: str):
    url = f"{GITHUB_API}/users/{username}/gists"

    async with httpx.AsyncClient(timeout=5.0) as client:
        response = await client.get(url)

    if response.status_code == 404:
        raise ValueError("GitHub user not found")

    response.raise_for_status()

    gists = response.json()

    return [
        {
            "id": gist["id"],
            "description": gist["description"],
            "html_url": gist["html_url"],
            "public": gist["public"],
            "created_at": gist["created_at"],
        }
        for gist in gists
    ]
