import requests
import responses
import json
import pytest
import os

# โหลดข้อมูล login จาก JSON
def load_login_data(filename):
    # หาตำแหน่งไฟล์ .py นี้ (test_mock_post_login_data.py)
    base = os.path.dirname(__file__)
    full_path = os.path.join(base, filename)

    with open(full_path, encoding="utf-8") as f:
        data = json.load(f)
        return [(i["username"], i["password"]) for i in data]

@responses.activate
@pytest.mark.parametrize("username, password", load_login_data("login_data.json"))
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
