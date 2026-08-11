import pytest
from app import app

print("hola")
@pytest.fixture
def client():
    # Configura el cliente de pruebas de la aplicación Flask
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_saludar_status_code(client):
    """Verifica que la ruta /saludar retorne un código de estado 200."""
    response = client.get("/saluda")
    assert response.status_code == 200


def test_ruta_no_existente_status_code(client):
    """Verifica que cualquier otra ruta (ej. /saludar2) retorne un código 404."""
    response = client.get("/saludar2")
    assert response.status_code == 404