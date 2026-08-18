import pytest
from api.posts_api import PostsAPI
from utils.assert_util import assert_status_code, assert_list_field

# 注意：这个测试函数需要接收 auth_token fixture
def test_get_posts_with_auth(auth_token):
    # 1. 实例化 PostsAPI
    posts_api = PostsAPI()
    # 2. 把从 fixture 拿到的 Token 塞进去
    posts_api.set_auth_token(auth_token)
    
    # 3. 请求 /posts（返回 100 条数据，但我们只取前 5 条做演示）
    response = posts_api.get("/posts?_limit=5")
    assert_status_code(response, 200)
    
    # 4. 批量校验前 5 条数据的 id 是否分别为 1,2,3,4,5
    assert_list_field(response, "id", [1, 2, 3, 4, 5])