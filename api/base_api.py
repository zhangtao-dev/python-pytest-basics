import requests
from config.settings import BASE_URL, TIMEOUT
# 导入我们 DAY7 写的日志工具
from utils.logger import setup_logger

# 给这个模块配一个专属日志记录器
logger = setup_logger("base_api")

class BaseAPI:
    def __init__(self):
        self.base_url = BASE_URL
        self.timeout = TIMEOUT
        self.session = requests.Session()

    def _request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        kwargs.setdefault("timeout", self.timeout)
        
        # 🟢 新增：请求前记一笔（行车记录仪开始录像）
        logger.info(f"🚀 发送请求: {method} {url}")
        
        response = self.session.request(method, url, **kwargs)
        
        # 🟢 新增：请求后记一笔（行车记录仪保存录像）
        logger.info(f"📥 收到响应: {method} {url} -> 状态码 {response.status_code}")
        
        return response

    def get(self, endpoint, **kwargs):
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self._request("POST", endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        return self._request("PUT", endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self._request("DELETE", endpoint, **kwargs)