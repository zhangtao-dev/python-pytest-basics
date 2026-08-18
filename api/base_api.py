import requests
from config.settings import BASE_URL, TIMEOUT
from utils.logger import setup_logger
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception

logger = setup_logger("base_api")

def is_retryable(response_or_exception):
    if isinstance(response_or_exception, requests.exceptions.RequestException):
        return True
    if hasattr(response_or_exception, 'status_code'):
        return response_or_exception.status_code >= 500
    return False

class BaseAPI:
    def __init__(self):
        self.base_url = BASE_URL
        self.timeout = TIMEOUT
        self.session = requests.Session()
        # 新增：默认请求头（后续可更新）
        self.session.headers.update({
            "Content-Type": "application/json"
        })

    def set_auth_token(self, token):
        """设置鉴权 Token，后续所有请求自动携带"""
        logger.info(f"🔑 设置全局 Token: {token[:10]}...")
        self.session.headers.update({
            "Authorization": f"Bearer {token}"
        })

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_fixed(1),
        retry=retry_if_exception(is_retryable)
    )
    def _request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        kwargs.setdefault("timeout", self.timeout)

        logger.info(f"🚀 发送请求: {method} {url}")
        # 打印当前请求头（方便调试，看看 Token 是否带上了）
        logger.info(f"📋 当前请求头: {self.session.headers}")
        
        response = self.session.request(method, url, **kwargs)
        logger.info(f"📥 收到响应: {method} {url} -> 状态码 {response.status_code}")

        if response.status_code >= 500:
            raise Exception(f"触发重试: {response.status_code}")
        return response

    def get(self, endpoint, **kwargs):
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self._request("POST", endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        return self._request("PUT", endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self._request("DELETE", endpoint, **kwargs)