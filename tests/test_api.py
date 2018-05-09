def test_currencies(client):
    response = client.get('/api/currencies')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert response.json == {'status': 'success', 'result': ['USD', 'EUR']}


def test_convert(client):
    response = client.get('/api/convert/1/USD/EUR')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert response.json['status'] == 'error'

    client.application.rates.update_rates({'USD': 1, 'EUR': 0.89, 'AUD': 2})
    response = client.get('/api/convert/1/USD/EUR')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert response.json == {'status': 'success', 'result': 0.89}

    response = client.get('/api/convert/1/EUR/USD')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert response.json == {'status': 'success', 'result': 1/0.89}

    response = client.get('/api/convert/1/EUR/AUD')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert response.json['status'] == 'error'
