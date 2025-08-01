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
    
    
    # TAREA SEMANA 3: Pruebas adicionales hecho por Leslie y Kevin


def test_delete_existing_item_with_httpx():
    #
    new_item = {"name": "Item to Delete", "description": "This is a test item."}
    post_response = httpx.post("http://localhost:8000/items/", json=new_item)
    assert post_response.status_code == 201

    item_id = post_response.json()["id"]
    delete_response = httpx.delete(f"http://localhost:8000/items/{item_id}")
    assert delete_response.status_code == 204

  
    get_response = httpx.get(f"http://localhost:8000/items/{item_id}")
    assert get_response.status_code == 404


def test_get_non_existent_item_error_with_httpx():
    non_existent_id = 9999
    response = httpx.get(f"http://localhost:8000/items/{non_existent_id}")
    assert response.status_code == 404
    assert response.json()["detail"] == f"Item with id {non_existent_id} not found"


def test_update_existing_item_with_httpx():
    
    new_item = {"name": "Item to Update", "description": "Original description."}
    post_response = httpx.post("http://localhost:8000/items/", json=new_item)
    assert post_response.status_code == 201
    
    item_id = post_response.json()["id"]
    updated_data = {"name": "Updated Name", "description": "New description."}

    put_response = httpx.put(f"http://localhost:8000/items/{item_id}", json=updated_data)
    assert put_response.status_code == 200

    
    get_response = httpx.get(f"http://localhost:8000/items/{item_id}")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Updated Name"
    assert get_response.json()["description"] == "New description."