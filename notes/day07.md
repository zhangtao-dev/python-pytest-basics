# DAY7：日志封装 + Excel 数据驱动

## 今日完成
- 封装了日志工具 `utils/logger.py`
- 使用 `openpyxl` 读取 Excel 数据文件
- 实现 Excel 数据驱动测试
- 4 个用例全部通过（4 passed）

## 学到的重要概念
- `logging` 模块：用 `INFO` / `WARNING` / `ERROR` 分级输出日志
- `openpyxl`：Python 读写 Excel 的标准库
- 数据源扩展：从 YAML 扩展到 Excel，测试代码不变

## 运行状态
- `pytest requests-demo/test_excel_driver.py -v -s` → 4 passed ✅

## 明天计划
- 整合 Week 1 内容，完成第一个里程碑
- 准备进入 Week 2：接口自动化框架实战