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

    import httpx
import pytest

# TAREA SEMANA 3: Pruebas adicionales hecho por la otra pareja

# Prueba 1: Verifica que se pueda obtener una lista de todos los ítems
def test_get_all_items_with_httpx():
    response = httpx.get("http://localhost:8000/api/v1/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Prueba 2: Verifica la creación de un ítem que incluye una descripción
def test_create_item_with_description():
    item_data = {
        "name": "Smartphone",
        "description": "Un nuevo smartphone de alta gama.",
        "price": 899.99,
        "is_offer": True
    }
    response = httpx.post("http://localhost:8000/api/v1/items/", json=item_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Smartphone"
    assert "description" in response.json()
    assert response.json()["description"] == "Un nuevo smartphone de alta gama."

# Prueba 3: Verifica un error esperado al actualizar un ítem con datos incorrectos
def test_update_item_with_invalid_price():
    # Primero, creamos un ítem para poder actualizarlo
    new_item = {"name": "Test Item", "description": "Original", "price": 100}
    post_response = httpx.post("http://localhost:8000/api/v1/items/", json=new_item)
    assert post_response.status_code == 200
    
    item_id = post_response.json()["id"]
    updated_data = {"name": "Updated Name", "price": "precio_invalido"}

    put_response = httpx.put(f"http://localhost:8000/api/v1/items/{item_id}", json=updated_data)
    assert put_response.status_code == 422
    assert "validation_error" in put_response.json()["detail"][0]["type"]
    