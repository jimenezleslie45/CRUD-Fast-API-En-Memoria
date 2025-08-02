import httpx
import pytest

def test_read_root():
    response = httpx.get("http://localhost:8000/")
    assert response.status_code == 200


def test_create_item_valid():
    item_data = {
        "name": "Mouse Gamer",
        "price": 75.0,
        "is_offer": True
    }
    response = httpx.post("http://localhost:8000/api/v1/items/", json=item_data)
    
    assert response.status_code == 200
    assert response.json()["name"] == "Mouse Gamer"
    assert response.json()["price"] == 75.0


def test_create_item_invalid():
    invalid_data = {
        "name": "Teclado",
        "price": "precio_invalido"
    }
    response = httpx.post("http://localhost:8000/api/v1/items/", json=invalid_data)
    
    assert response.status_code == 422
    assert "validation_error" in response.json()["detail"][0]["type"]