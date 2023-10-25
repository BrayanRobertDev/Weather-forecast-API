import json
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_temperature_city(client):
    response = client.get('/city_temperature/Rio de Janeiro')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['city'] == 'Rio de Janeiro'

def test_not_found_error(client):
    response = client.get('/non_existent_route')
    data = json.loads(response.data)
    assert response.status_code == 404
    assert data['error'] == 'Página não encontrada'

def test_internal_server_error(client):
    response = client.get('/city_temperature/InvalidCityName')
    data = json.loads(response.data)
    assert response.status_code == 500
    assert data['error'] == "Name InvalidCityName is invalid."
