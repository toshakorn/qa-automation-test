import requests
import responses

@responses.activate
def test_mocked_api_response():
    # Mock URL + Response
    responses.add(
        method=responses.GET,
        url="https://api.example.com/user/1",
        json={"id": 1, "name": "Mock User"},
        status=200
    )

    # ใช้จริง
    response = requests.get("https://api.example.com/user/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Mock User"
    print("✅ Mocked API call successful!")
