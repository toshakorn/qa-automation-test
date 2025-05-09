import requests
import responses
import json
import pytest

# โหลดข้อมูล login จาก JSON
def load_login_data(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
        return [(i["username"], i["password"]) for i in data]

@pytest.mark.parametrize("username, password", load_login_data("testApi/login_data.json"))
@responses.activate
def test_mock_login(username, password):
    def request_callback(request):
        body = json.loads(request.body)
        if body["username"] == "kminchelle" and body["password"] == "0lelplR":
            return (200, {}, json.dumps({"token": "mocked-token"}))
        else:
            return (401, {}, json.dumps({"error": "Invalid credentials"}))

    responses.add_callback(
        responses.POST,
        "https://dummyjson.com/auth/login",
        callback=request_callback,
        content_type="application/json"
    )

    # เรียกใช้ API ที่ mock ไว้
    res = requests.post("https://dummyjson.com/auth/login", json={
        "username": username,
        "password": password
    })

    # ตรวจผลลัพธ์
    if username == "kminchelle" and password == "0lelplR":
        assert res.status_code == 200
        assert "token" in res.json()
        print(f"✅ Login success: {username}")
    else:
        assert res.status_code == 401
        print(f"❌ Login failed: {username} ({res.status_code})")
