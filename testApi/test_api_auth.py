import requests
from requests.auth import HTTPBasicAuth

def test_basic_auth_success():
    response = requests.get(
        "https://httpbin.org/basic-auth/user/passwd",
        auth=HTTPBasicAuth("user", "passwd")
    )
    assert response.status_code == 200
    assert response.json()["authenticated"] is True
    assert response.json()["user"] == "user"

def test_basic_auth_fail():
    response = requests.get(
        "https://httpbin.org/basic-auth/user/passwd",
        auth=HTTPBasicAuth("user", "wrongpass")
    )
    assert response.status_code == 401  # Unauthorized
