import pytest
from api.posts_api import PostsAPI

posts_api = PostsAPI()

def test_get_post():
    response = posts_api.get_post(1)
    assert response.status_code == 200
    assert response.json()["id"] == 1

@pytest.mark.parametrize("post_id", [1, 2])
def test_get_multiple_posts(post_id):
    response = posts_api.get_post(post_id)
    assert response.status_code == 200
    assert response.json()["id"] == post_id

@pytest.mark.parametrize("title", ["框架测试1", "框架测试2"])
def test_create_post(title):
    response = posts_api.create_post(title, "这是用新框架创建的")
    assert response.status_code == 201
    assert response.json()["title"] == title

def test_update_post():
    response = posts_api.update_post(1, title="已更新的标题")
    assert response.status_code == 200
    assert response.json()["title"] == "已更新的标题"
