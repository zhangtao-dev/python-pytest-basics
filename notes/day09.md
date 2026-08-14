# DAY9：核心封装层开发

## 今日完成
- `BaseAPI` 集成日志（自动记录请求/响应状态码）
- 封装 `utils/assert_util.py`：智能断言工具（状态码 + JSON 字段）
- 重构 `testcases/test_posts.py`，改用智能断言
- 6 个用例全部通过（6 passed）

## 学到的重要概念
- **自动日志**：底层封装一次，所有接口自动继承，不用在每个用例里写 print
- **智能断言**：封装 assert，报错时输出清晰对比，并提示字段是否存在
- **代码分层**：测试用例只关心业务语义，不关心底层请求和日志实现

## 运行状态
- `pytest testcases/test_posts.py -v -s` → 6 passed ✅

## 明天计划
- 继续完善核心封装层（封装 DBUtil 或 请求重试机制）
- 开始接入毕业设计 API 接口