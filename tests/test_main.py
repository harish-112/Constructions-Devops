import httpx
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from app.main import app

# Modern explicit initialization that supports newer HTTPX/Starlette versions
client = TestClient(transport=httpx.ASGITransport(app=app), base_url="http://test")

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "running"

def test_get_projects_returns_list():
    mock_db = MagicMock()
    mock_db.query.return_value.all.return_value = []
    with patch("app.main.get_db", return_value=iter([mock_db])):
        response = client.get("/projects")
        assert response.status_code == 200
