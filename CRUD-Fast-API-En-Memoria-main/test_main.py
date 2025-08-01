import httpx

def test_read_root():
    response = httpx.get("http://localhost:8000/")
    assert response.status_code == 200

def test_create_item_valid():
    item_data = {
        "name": "Laptop",
        "price": 1200.50,
        "is_offer": False
    }
    response = httpx.post("http://localhost:8000/items/", json=item_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Laptop"
    assert response.json()["price"] == 1200.50

def test_create_item_invalid():
    invalid_data = {
        "name": "Tablet",
        "price": "precio_invalido"
    }
    response = httpx.post("http://localhost:8000/items/", json=invalid_data)
    assert response.status_code == 422