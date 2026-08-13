import requests
from config.settings import BASE_URL, TIMEOUT

class BaseAPI:
    def __init__(self):
        self.base_url = BASE_URL
        self.timeout = TIMEOUT
        self.session = requests.Session()

    def _request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        kwargs.setdefault("timeout", self.timeout)
        return self.session.request(method, url, **kwargs)

    def get(self, endpoint, **kwargs):
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self._request("POST", endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        return self._request("PUT", endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self._request("DELETE", endpoint, **kwargs)
