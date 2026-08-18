import pytest
from app import app

@pytest.fixture
def client():
    # Configura el cliente de pruebas de la aplicación Flask
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_saludar_status_code(client):
    """Verifica que la ruta /saludar retorne un código de estado 200."""
    response = client.get("/saludar")
    assert response.status_code == 200
    saludo = response.get_json()["saludo"]
    print(saludo)

def test_cachipun_status_code(client):
    response = client.get("/cachipun")
    assert response.status_code == 200
    mensaje = response.get_json()["mensaje"]
    assert mensaje in ["Piedra", "Papel", "Tijera"]
    print(mensaje)


def test_ruta_no_existente_status_code(client):
    """Verifica que cualquier otra ruta (ej. /saludar2) retorne un código 404."""
    response = client.get("/saludar2")
    assert response.status_code == 404