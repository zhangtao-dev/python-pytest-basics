import pytest

@pytest.fixture
def sample_data():
    print("\n[Setup] 正在准备测试数据...")
    data = {"name": "admin", "age": 30}
    yield data
    print("[Teardown] 清理测试数据...")

def test_user_info(sample_data):
    assert sample_data["name"] == "admin"
    assert sample_data["age"] == 30
    print("测试中...正在校验数据")

def test_user_age_not_zero(sample_data):
    assert sample_data["age"] > 0