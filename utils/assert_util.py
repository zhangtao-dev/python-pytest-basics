from utils.logger import setup_logger

logger = setup_logger("assert_util")

def assert_status_code(response, expected_code):
    logger.info(f"🔍 验证状态码：预期 {expected_code}，实际 {response.status_code}")
    assert response.status_code == expected_code, \
        f"❌ 状态码不匹配！期望 {expected_code}，实际返回 {response.status_code}"

def assert_json_value(response, key, expected_value):
    try:
        actual_value = response.json().get(key)
    except Exception:
        actual_value = None

    logger.info(f"🔍 验证字段 '{key}'：预期 '{expected_value}'，实际 '{actual_value}'")

    if actual_value is None:
        available_keys = list(response.json().keys()) if response.text else []
        raise AssertionError(
            f"❌ 字段 '{key}' 不存在于返回数据中！当前返回的字段有：{available_keys}"
        )

    assert actual_value == expected_value, \
        f"❌ 字段 '{key}' 值不匹配！期望 '{expected_value}'，实际 '{actual_value}'"

def assert_list_field(response, key, expected_values):
    """
    批量校验列表数据中某个字段的值
    response: 请求返回的响应对象
    key: 要校验的字段名（如 "id"）
    expected_values: 期望的列表值（如 [1, 2, 3]）
    """
    logger.info(f"🔍 批量校验列表字段 '{key}'，预期长度 {len(expected_values)}")
    
    data = response.json()
    # 如果返回的数据不是列表，尝试取出列表（比如放在 'data' 字段里）
    if not isinstance(data, list):
        # 常见情况：数据包裹在 data 字段里
        if isinstance(data, dict) and "data" in data:
            data = data["data"]
        else:
            raise AssertionError(f"❌ 响应数据不是列表，类型为 {type(data)}")
    
    actual_values = [item.get(key) for item in data]
    logger.info(f"📊 实际取到的字段值: {actual_values}")
    
    assert actual_values == expected_values, \
        f"❌ 列表字段 '{key}' 值不匹配！期望 {expected_values}，实际 {actual_values}"