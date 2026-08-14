# utils/assert_util.py
from utils.logger import setup_logger

logger = setup_logger("assert_util")

def assert_status_code(response, expected_code):
    """验证状态码，报错时输出清晰对比"""
    logger.info(f"🔍 验证状态码：预期 {expected_code}，实际 {response.status_code}")
    assert response.status_code == expected_code, \
        f"❌ 状态码不匹配！期望 {expected_code}，实际返回 {response.status_code}"

def assert_json_value(response, key, expected_value):
    """验证 JSON 字段值，报错时输出清晰对比，并提示字段是否存在"""
    try:
        actual_value = response.json().get(key)
    except Exception:
        actual_value = None
    
    logger.info(f"🔍 验证字段 '{key}'：预期 '{expected_value}'，实际 '{actual_value}'")
    
    # 友善提示：如果字段不存在（返回 None），给出明确报错
    if actual_value is None:
        available_keys = list(response.json().keys()) if response.text else []
        raise AssertionError(
            f"❌ 字段 '{key}' 不存在于返回数据中！当前返回的字段有：{available_keys}"
        )
    
    assert actual_value == expected_value, \
        f"❌ 字段 '{key}' 值不匹配！期望 '{expected_value}'，实际 '{actual_value}'"