from fastapi import FastAPI, HTTPException
from app.github import fetch_public_gists

app = FastAPI(title="GitHub Gists API")

@app.get("/{username}")
async def get_user_gists(username: str):
    try:
        gists = await fetch_public_gists(username)
        return gists
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except Exception:
        raise HTTPException(
            status_code=502,
            detail="Failed to fetch data from GitHub"
        )
