import functools

def my_fixture(func):
    func._is_fixture = True
    return func

def my_fixture_with_teardown(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[Setup] 准备执行 {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[Teardown] 清理 {func.__name__} 的资源")
        return result
    return wrapper

@my_fixture
def db_conn():
    return {"host": "localhost", "port": 3306}

@my_fixture_with_teardown
def get_user():
    print("  正在获取用户数据...")
    return {"name": "admin", "role": "sdet"}

if __name__ == "__main__":
    print("=== 装饰器原理演示 ===\n")
    print(f"db_conn 是 fixture 吗？ {getattr(db_conn, '_is_fixture', False)}")
    print(f"数据: {db_conn()}\n")
    print("--- 带 Teardown 的 Fixture ---")
    print(f"用户: {get_user()}")