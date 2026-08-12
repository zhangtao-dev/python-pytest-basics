import pytest
import openpyxl
from utils.logger import setup_logger

logger = setup_logger("excel_driver")

def load_excel_data(file_path):
    wb = openpyxl.load_workbook(file_path)
    ws = wb.active
    data = []
    for row in ws.iter_rows(min_row=2, values_only=True):
        method, endpoint, expected_code = row
        data.append((method, endpoint, expected_code))
    return data

excel_cases = load_excel_data("data/test_data.xlsx")

@pytest.mark.parametrize("method, endpoint, expected_code", excel_cases)
def test_api_from_excel(api_client, method, endpoint, expected_code):
    logger.info(f"开始测试：{method} {endpoint}，期望状态码：{expected_code}")
    response = api_client(method, endpoint)
    logger.info(f"实际状态码：{response.status_code}")
    assert response.status_code == expected_code
    logger.info(f"✅ 测试通过：{method} {endpoint}")
