from api.base_api import BaseAPI

class UserAPI(BaseAPI):
    def login(self, username, password):
        # 利用 /posts 接口模拟登录，它将回显你提交的数据
        endpoint = "/posts"
        payload = {
            "title": username,    # 用 title 存用户名
            "body": password,     # 用 body 存密码
            "userId": 1
        }
        return self.post(endpoint, json=payload)