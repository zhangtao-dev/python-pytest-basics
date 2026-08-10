# DAY5：接口测试框架封装

## 今日完成
- 修复 `conftest.py` 语法错误（补齐逗号、修正函数名）
- 在 `conftest.py` 中新增 `base_url` 和 `api_client` Fixture
- 在 `requests-demo` 下新建 `test_api.py`，写出 6 个接口测试用例
- 全部用例通过（6 passed）

## 学到的重要概念
- 接口测试的本质：调网址 + 看返回 + 写断言
- `conftest.py` = 全局工具箱，统一管理地址和请求方式
- `api_client` 封装了发请求的细节，测试函数只关心业务逻辑
- `@pytest.mark.parametrize` 让一个用例跑多组数据

## 运行状态
- `pytest requests-demo/test_api.py -v` → 6 passed ✅

## 明天计划
- 数据驱动与配置外置（将测试数据移到 YAML 文件）