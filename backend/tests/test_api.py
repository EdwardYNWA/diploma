import requests

BASE_URL = "http://127.0.0.1:5000"

def test_get_test():
    response = requests.get(f"{BASE_URL}/test")
    assert response.status_code == 200
