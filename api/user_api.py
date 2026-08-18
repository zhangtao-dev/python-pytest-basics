from api.base_api import BaseAPI

class UserAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.base_url = "https://dummyjson.com"

    def login(self, username, password):
        endpoint = "/auth/login"
        payload = {
            "username": username,
            "password": password
        }
        return self.post(endpoint, json=payload)