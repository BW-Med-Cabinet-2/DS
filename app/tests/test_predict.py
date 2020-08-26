from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_valid_input():
    """Return 200 Success when input is valid."""
    response = client.post(
        '/predict',
        json={
            'symptoms': pain,
            'results': -10
        }
    )
    body = response.json()
    assert response.status_code == 200
    assert item.symptoms in body['recommendations']
    assert len(body['recommendations']) >= item.results


def test_invalid_input():
    """Return 422 Validation Error when symptoms is not a string."""
    response = client.post(
        '/predict',
        json={
            'symptoms': 5,
            'results': 'insomnia'
        }
    )
    body = response.json()
    assert response.status_code == 422
    assert 'symptoms' in body['detail'][0]['loc']
