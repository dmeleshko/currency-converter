import pytest

from app import create_app
from config import Config


class TestConfig(Config):
    TESTING = True
    CURRENCIES = ['USD', 'EUR']


@pytest.fixture
def test_client():
    app = create_app(TestConfig)
    return app.test_client()


def test_currencies(test_client):
    response = test_client.get('/api/currencies')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert response.json == {'status': 'success', 'result': ['USD', 'EUR']}


def test_convert(test_client):
    response = test_client.get('/api/convert/1/USD/EUR')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert response.json['status'] == 'error'

    test_client.application.rates.update_rates({'USD': 1, 'EUR': 0.89, 'AUD': 2})
    response = test_client.get('/api/convert/1/USD/EUR')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert response.json == {'status': 'success', 'result': 0.89}

    response = test_client.get('/api/convert/1/EUR/USD')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert response.json == {'status': 'success', 'result': 1/0.89}

    response = test_client.get('/api/convert/1/EUR/AUD')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert response.json['status'] == 'error'