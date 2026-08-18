# DAY11：Token管理与批量数据校验

## 今日完成
- `BaseAPI` 支持动态设置 Token（`set_auth_token`）
- `conftest.py` 实现全局登录 Fixture（`scope="session"`，一次登录全局复用）
- `utils/assert_util.py` 新增 `assert_list_field`（批量校验列表字段）
- `testcases/test_auth_posts.py` 演示带 Token 的请求 + 批量校验

## 学到的重要概念
- **Token 自动携带**：一次设置，所有请求自动带上，测试用例无需关心鉴权细节
- **全局登录**：`scope="session"` 使登录只执行一次，大幅提升测试效率
- **批量校验**：`assert_list_field` 让列表数据验证从 N 行变为 1 行

## 运行状态
- `pytest testcases/test_auth_posts.py -v -s` → 1 passed ✅

## 明天计划
- 开始封装毕业设计（校园活动管理系统）的 5 个业务模块接口
- 用今天学到的 Token 机制为所有接口自动鉴权