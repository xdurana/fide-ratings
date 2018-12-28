import requests

def test_api():
    r = requests.get('http://localhost:5000/api')
    assert r.status_code == 200
    assert True
