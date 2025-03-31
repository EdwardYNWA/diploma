import requests

BASE_URL = "http://127.0.0.1:5000"

def test_get_test():
    response = requests.get(f"{BASE_URL}/test")
    print("Статус код:", response.status_code)
    print("Ответ:", response.text)
    assert response.status_code == 200

test_get_test()
