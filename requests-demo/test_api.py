import pytest

def test_get_post(api_client):
    response = api_client("GET", "/posts/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

@pytest.mark.parametrize("post_id", [1, 2])
def test_get_multiple_posts(api_client, post_id):
    response = api_client("GET", f"/posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["id"] == post_id

@pytest.mark.parametrize("title", ["foo", "bar"])
def test_create_post(api_client, title):
    payload = {"title": title, "body": "content", "userId": 1}
    response = api_client("POST", "/posts", json=payload)
    assert response.status_code == 201
    assert response.json()["title"] == title

def test_update_post(api_client):
    payload = {"id": 1, "title": "updated title"}
    response = api_client("PUT", "/posts/1", json=payload)
    assert response.status_code == 200
    assert response.json()["title"] == "updated title"