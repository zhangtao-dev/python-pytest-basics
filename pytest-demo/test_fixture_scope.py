import pytest

@pytest.fixture(scope="session")
def global_resource():
    print("\n[Global Setup] 创建全局资源（仅一次）...")
    yield "DB_CONNECTION"
    print("[Global Teardown] 释放全局资源（仅一次）...")

@pytest.fixture
def per_function_resource():
    print("[Function Setup] 每次函数都创建...")
    yield "temp_file"
    print("[Function Teardown] 每次函数都清理...")

def test_a(global_resource, per_function_resource):
    print("执行 test_a")
    assert global_resource == "DB_CONNECTION"

def test_b(global_resource, per_function_resource):
    print("执行 test_b")
    assert True