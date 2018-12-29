import requests

def test_api():
    r = requests.get('http://127.0.0.1:5000/api/')
    assert r.status_code == 200
    assert True
