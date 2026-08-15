# DAY10：核心封装层深化 + 登录接口实战

## 今日完成
- 在 `api/user_api.py` 中封装 `UserAPI` 类，实现 `login` 方法
- 在 `testcases/test_login.py` 中编写登录测试用例（1 个成功场景）
- 验证 `BaseAPI` 的自动重试与日志记录功能
- 登录测试通过（201 状态码，字段断言正确）

## 学到的重要概念
- **接口封装**：将具体的接口地址和请求参数封装在 API 类中，测试用例只关心业务动作
- **依赖注入**：测试用例通过调用封装好的 `login` 方法，无需关心底层实现
- **框架可迁移性**：更换 `BASE_URL` 和 `endpoint` 即可将测试目标从公共 API 切换到真实项目

## 运行状态
- `pytest testcases/test_login.py -v -s` → 1 passed ✅

## 明天计划
- 实现 Token 自动携带（结合 `scope="session"` fixture）
- 封装列表数据校验工具