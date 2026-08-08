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