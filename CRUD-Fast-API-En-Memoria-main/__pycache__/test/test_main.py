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
    response = httpx.post("http://localhost:8000/api/v1/items/", json=item_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Laptop"
    assert response.json()["price"] == 1200.50

def test_create_item_invalid():
    invalid_data = {
        "name": "Tablet",
        "price": "precio_invalido"
    }
    response = httpx.post("http://localhost:8000/api/v1/items/", json=invalid_data)
    assert response.status_code == 422

# --- Tarea: Pruebas adicionales para la semana 3 --- Leslie

# 1. Agrega al menos tres nuevos casos de prueba a tu archivo test_main.py.

# Prueba adicional 1: 
def test_create_item_with_description():
    new_item = {
        "name": "Mesa de escritorio",
        "price": 99.99,
        "description": "Mesa de madera para oficina en casa."
    }
    response = httpx.post("http://localhost:8000/api/v1/items/", json=new_item)
    assert response.status_code == 200
    assert "description" in response.json()
    assert response.json()["description"] == "Mesa de madera para oficina en casa."

# 2. Al menos uno debe probar un error esperado (ej. datos faltantes o inválidos).

# Prueba adicional 2: 
def test_update_item_with_invalid_price():
    
    post_response = httpx.post("http://localhost:8000/api/v1/items/", json={"name": "Temp Item", "price": 10})
    assert post_response.status_code == 200
    item_id = post_response.json()["id"]

    invalid_update_data = {"price": "precio-texto"}
    put_response = httpx.put(f"http://localhost:8000/api/v1/items/{item_id}", json=invalid_update_data)
    
    # Usamos assert para verificar el código de estado HTTP 422
    assert put_response.status_code == 422

# Prueba adicional 3: Verifica que la API devuelve un error 404 al intentar eliminar un ítem inexistente
def test_delete_non_existent_item_error():
    non_existent_id = 99999
    response = httpx.delete(f"http://localhost:8000/api/v1/items/{non_existent_id}")
    
    # Usamos assert para verificar el código de estado HTTP 404
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()
