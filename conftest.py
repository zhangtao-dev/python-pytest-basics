from utils.logger import setup_logger
import pytest

@pytest.fixture(scope="session")
def global_config():
    print("\n[conftest] 加载全局配置...")
    config = {
        "base_url": "https://api.example.com",
        "timeout": 30
    }
    yield config
    print("[conftest] 清理全局配置...")

@pytest.fixture
def test_user():
    return {"name": "admin", "password": "123456"}



import requests

@pytest.fixture(scope="session")
def base_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture
def api_client(base_url):
    def _request(method, endpoint, **kwargs):
        url = f"{base_url}{endpoint}"
        return requests.request(method, url, **kwargs)
    return _request

import pytest
import requests
from utils.logger import setup_logger
from api.user_api import UserAPI

# 如果你之前有 global_config、test_user 等 fixture，保留它们，不要覆盖。
# 以下为新增的 auth_token fixture：

@pytest.fixture(scope="session")
def auth_token():
    logger = setup_logger("auth_fixture")
    logger.info("🔐 开始执行全局登录（仅一次）...")
    user_api = UserAPI()
    response = user_api.login("emilys", "emilyspass")
    assert response.status_code == 200, f"登录失败：{response.status_code}"
    json_data = response.json()
    logger.info(f"登录响应体: {json_data}")
    token = json_data["accessToken"]   # 改为 accessToken
    logger.info(f"✅ 登录成功，获取 Token: {token}")
    return token