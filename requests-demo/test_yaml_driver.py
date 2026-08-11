import pytest
import yaml

def load_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

data = load_yaml('data/test_data.yaml')
get_ids = data['get_posts']
create_data = data['create_posts']

def test_get_from_yaml(api_client):
    post_id = get_ids[0]
    response = api_client("GET", f"/posts/{post_id}")
    assert response.status_code == 200

@pytest.mark.parametrize("post_id", get_ids)
def test_get_multiple_from_yaml(api_client, post_id):
    response = api_client("GET", f"/posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["id"] == post_id

@pytest.mark.parametrize("item", create_data)
def test_create_from_yaml(api_client, item):
    payload = {
        "title": item["title"],
        "body": item["body"],
        "userId": 1
    }
    response = api_client("POST", "/posts", json=payload)
    assert response.status_code == 201
    assert response.json()["title"] == item["title"]