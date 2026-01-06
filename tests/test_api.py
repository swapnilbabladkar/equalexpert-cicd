from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_gists_for_octocat():
    response = client.get("/octocat")

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)

    if data:
        gist = data[0]
        assert "id" in gist
        assert "html_url" in gist
        assert "public" in gist
