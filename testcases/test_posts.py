import pytest
from api.posts_api import PostsAPI
# 导入我们刚封装的“智能尺子”
from utils.assert_util import assert_status_code, assert_json_value

posts_api = PostsAPI()

def test_get_post():
    response = posts_api.get_post(1)
    # 用工具验证，而不是原始 assert
    assert_status_code(response, 200)
    assert_json_value(response, "id", 1)

@pytest.mark.parametrize("post_id", [1, 2])
def test_get_multiple_posts(post_id):
    response = posts_api.get_post(post_id)
    assert_status_code(response, 200)
    assert_json_value(response, "id", post_id)

@pytest.mark.parametrize("title", ["框架测试1", "框架测试2"])
def test_create_post(title):
    response = posts_api.create_post(title, "这是用新框架创建的")
    assert_status_code(response, 201)
    assert_json_value(response, "title", title)

def test_update_post():
    response = posts_api.update_post(1, title="已更新的标题")
    assert_status_code(response, 200)
    assert_json_value(response, "title", "已更新的标题")