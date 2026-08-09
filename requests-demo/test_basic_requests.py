import requests

# 目标：测试 JSONPlaceholder 的 API（免费假接口）
BASE_URL = "https://jsonplaceholder.typicode.com"

# 1. 测试 GET 请求（获取单个资源）
def test_get_post():
    response = requests.get(f"{BASE_URL}/posts/1")
    
    # 断言 1：状态码必须是 200
    assert response.status_code == 200
    
    # 断言 2：返回的 JSON 数据必须包含 'id' 字段，且值为 1
    data = response.json()
    assert data["id"] == 1
    assert data["userId"] == 1
    print(f"✅ GET 测试通过，标题为：{data['title'][:30]}...")

# 2. 测试 POST 请求（创建资源）
def test_create_post():
    new_data = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=new_data)
    
    # 断言：创建成功应该返回 201（Created）状态码
    assert response.status_code == 201
    
    data = response.json()
    # 断言：返回的数据里应该包含我们刚传的 title
    assert data["title"] == "foo"
    print(f"✅ POST 测试通过，新资源 ID 为：{data['id']}")

# 3. 测试 Session 携带 Header（模拟携带 Token）
def test_with_headers():
    session = requests.Session()
    # 设置通用的请求头（比如模拟浏览器、携带 Token）
    session.headers.update({
        "User-Agent": "MyTestClient/1.0",
        "Authorization": "Bearer fake_token_123"
    })
    
    response = session.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    print("✅ Session 携带 Header 测试通过")