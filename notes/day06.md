# DAY6：数据驱动与配置外置

## 今日完成
- 安装 `pyyaml` 库，用于解析 YAML 文件
- 在项目根目录下新建 `data/` 文件夹，并在其中创建 `test_data.yaml`
- 在 `requests-demo` 下新建 `test_yaml_driver.py`
- 实现从 YAML 文件读取测试数据，并通过 `@pytest.mark.parametrize` 驱动测试
- 5 个测试用例全部通过（5 passed）

## 学到的重要概念
- 数据驱动测试：同一套测试逻辑，用不同的数据跑多次
- YAML：一种配置文件格式，用缩进表示层级，天然对应 Python 的字典和列表
- 配置外置：把测试数据从代码中抽离，放到外部文件，改数据不用改代码

## 运行状态
- `pytest requests-demo/test_yaml_driver.py -v` → 5 passed ✅

## 明天计划
- 日志封装（logging 模块）
- 接入 Excel 数据源