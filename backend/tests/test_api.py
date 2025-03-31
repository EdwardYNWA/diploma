import requests

BASE_URL = "http://127.0.0.1:5000"

def test_get_test():
    response = requests.get(f"{BASE_URL}/test", headers={"Content-Type": "application/json"})
    print(response.status_code, response.text)  # Выведет код ответа и текст ошибки, если есть
    assert response.status_code == 200

test_get_test()
