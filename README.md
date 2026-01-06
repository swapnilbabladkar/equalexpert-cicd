# GitHub Gists API – Operability Take-Home Exercise

A simple HTTP API that returns a list of publicly available GitHub Gists for a given user.

This project is intentionally minimal, easy to run, and containerised with sensible defaults to support operability and maintainability.

---

## API Overview

### Endpoint

```
GET /<github_username>
```

### Example

```bash
curl http://localhost:8080/octocat
```

### Response

Returns a JSON array of public gists for the specified user.

```json
[
  {
    "id": "gist_id",
    "description": "Example gist",
    "html_url": "https://gist.github.com/...",
    "public": true,
    "created_at": "2023-01-01T00:00:00Z"
  }
]
```

### Error Handling

- `404` – GitHub user not found  
- `502` – Failure communicating with GitHub API

---

## Requirements

### For local development
- Python **3.11+**
- pip
- Virtual environment support

### For containerised execution
- Docker-compatible runtime  
  (Docker Desktop, Colima, or equivalent)

---

## Local Development

### Setup virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the API

```bash
uvicorn app.main:app --port 8080
```

### Test locally

```bash
curl http://localhost:8080/octocat
```

---

## Running Tests

Tests validate the API using a real public GitHub user (`octocat`).

```bash
python -m pytest
```

> Note: A deprecation warning from `httpx` may appear during test runs.  
> This originates from FastAPI’s test client internals and does not affect functionality.

---

## Docker

The application is packaged as a Docker container and listens on **port 8080**.

- Multi-stage build  
- Runs as a **non-root user**  
- No system-wide configuration changes required  

---

### Apple Silicon (M1 / M2 / M3)

Docker has been tested using **Colima** on Apple Silicon.

Start Colima:

```bash
colima start
```

Ensure Docker is using the Colima context:

```bash
docker context use colima
```

Build the image:

```bash
docker build -t github-gists-api .
```

If an explicit platform is required:

```bash
docker build --platform linux/arm64 -t github-gists-api .
```

Run the container:

```bash
docker run -p 8080:8080 github-gists-api
```

---

### Non-Apple Silicon (Intel / x86_64)

Standard Docker Desktop or compatible Docker runtimes can be used.

Build the image:

```bash
docker build -t github-gists-api .
```

Run the container:

```bash
docker run -p 8080:8080 github-gists-api
```

---

### Verify Runtime User (Optional)

The container runs as a non-root user.

```bash
docker ps
docker exec -it <container_id> id
```

Expected output will show a non-root UID.

---

## Notes

- Only **public GitHub Gists** are accessed  
- No authentication or GitHub tokens are required  
- The solution intentionally avoids unnecessary dependencies or complexity  

---

## Project Structure

```
.
├── app
│   ├── __init__.py
│   ├── main.py
│   └── github.py
├── tests
│   └── test_api.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## Summary

This solution focuses on:
- Simplicity and clarity
- Testability
- Container best practices
- Cross-platform compatibility

The goal is to make the service easy to understand, easy to run, and easy to review.
