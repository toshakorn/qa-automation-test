import requests
import pytest
import json

def load_login_data(file_path):
    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)
        return [(item["email"], item["password"]) for item in data]

@pytest.mark.parametrize("email, password", load_login_data("testApi/login_data.json"))
def test_login_api(email, password):
    url = "https://dummyjson.com/auth/login"
    # URL for the login API
    headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
    }
    payload = {"email": email, "password": password}

    response = requests.post(url, headers=headers, json=payload)
    print("Response body:", response.text)
    if email == "eve.holt@reqres.in" and password == "cityslicka":
        assert response.status_code == 200
        assert "token" in response.json()
        print(f"✅ Login Success: {email}")
    else:
        assert response.status_code in [400, 401]
        print(f"❌ Login Failed: {email} ({response.status_code})")
