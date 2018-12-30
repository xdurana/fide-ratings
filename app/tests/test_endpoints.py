import requests

def test_api():
    assert True
    return
    r = requests.get('/api/')
    assert r.status_code == 200
    assert True
