import json
import pytest
from app import app

class TestApp:
    @pytest.fixture
    def client(self):
        app.config['TESTING'] = True
        client = app.test_client()
        yield client

    def test_add_data(self, client):
        data = {'data': 'test_data'}
        response = client.post('/add', json=data)
        assert response.status_code == 200
        assert json.loads(response.data) == {'status': 'success'}

    def test_add_data_invalid_input(self, client):
        invalid_data = {'invalid_key': 'test_data'}
        response = client.post('/add', json=invalid_data)
        assert response.status_code == 500
        assert 'error' in json.loads(response.data)

    def test_get_data(self, client):
        response = client.get('/get')
        assert response.status_code == 200
