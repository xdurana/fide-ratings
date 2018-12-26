import requests

def test_api():
    r = requests.get('http://localhost')
    assert r.status_code == 200
    assert True
