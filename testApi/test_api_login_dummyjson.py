import requests
import pytest
import json

def load_login_data(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
        return [(i["username"], i["password"]) for i in data]

@pytest.mark.parametrize("username, password", load_login_data("testApi/login_data.json"))
def test_login_dummyjson(username, password):
    url = "https://dummyjson.com/auth/login"
    headers = {"Content-Type": "application/json"}
    payload = {"username": username, "password": password}

    response = requests.post(url, headers=headers, json=payload)
    print("Response body:", response.text)

    if response.status_code == 200:
        assert "accessToken" in response.json()
        print(f"✅ Login Success: {username}")
    else:
        assert response.status_code in [400, 401]
        print(f"❌ Login Failed: {username} ({response.status_code})")
