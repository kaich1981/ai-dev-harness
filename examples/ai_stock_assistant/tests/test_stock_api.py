import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_analyze_success(client):
    resp = client.post("/api/stock/analyze", json={
        "stock_code": "AAPL",
        "cost_price": 180.0,
    })
    assert resp.status_code == 200
    data = resp.json()
    assert data["stock_code"] == "AAPL"
    assert data["trend"] in ("up", "down", "stable")
    assert 0 <= data["confidence"] <= 1
    assert len(data["suggestion"]) > 0
    assert len(data["risk_note"]) > 0


def test_analyze_invalid_price(client):
    resp = client.post("/api/stock/analyze", json={
        "stock_code": "AAPL",
        "cost_price": -10,
    })
    assert resp.status_code == 422


def test_analyze_missing_field(client):
    resp = client.post("/api/stock/analyze", json={
        "stock_code": "AAPL",
    })
    assert resp.status_code == 422


def test_history_after_analyze(client):
    # Create an analysis first
    client.post("/api/stock/analyze", json={
        "stock_code": "TSLA",
        "cost_price": 250.0,
    })
    resp = client.get("/api/stock/history", params={"stock_code": "TSLA"})
    assert resp.status_code == 200
    data = resp.json()
    assert len(data["items"]) >= 1
    assert data["items"][0]["stock_code"] == "TSLA"


def test_history_empty(client):
    resp = client.get("/api/stock/history", params={"stock_code": "NONEXIST"})
    assert resp.status_code == 200
    assert resp.json()["items"] == []
