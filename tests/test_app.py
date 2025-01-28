import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_post_receipt_process():
    """Test submitting a receipt and getting an ID."""
    response = client.post(
        "/receipts/process",
        json={
            "retailer": "Target",
            "purchaseDate": "2023-01-01",
            "purchaseTime": "15:30",
            "total": "35.25",
            "items": [
                {"shortDescription": "Pepsi", "price": "1.25"},
                {"shortDescription": "Lays", "price": "3.00"}
            ]
        },
    )

    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert isinstance(data["id"], str)

def test_get_receipt_points():
    """Test retrieving points for a processed receipt."""
    # To submit a new receipt first time
    post_response = client.post(
        "/receipts/process",
        json={
            "retailer": "Target",
            "purchaseDate": "2023-01-01",
            "purchaseTime": "15:30",
            "total": "35.25",
            "items": [
                {"shortDescription": "Pepsi", "price": "1.25"},
                {"shortDescription": "Lays", "price": "3.00"}
            ]
        },
    )

    receipt_id = post_response.json()["id"]

    # Fetch points for the generated receipt ID we are using
    get_response = client.get(f"/receipts/{receipt_id}/points")

    assert get_response.status_code == 200
    data = get_response.json()
    assert "points" in data
    assert data["points"] == 54  
