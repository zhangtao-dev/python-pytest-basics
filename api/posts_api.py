from api.base_api import BaseAPI

class PostsAPI(BaseAPI):
    def get_post(self, post_id):
        return self.get(f"/posts/{post_id}")

    def create_post(self, title, body, user_id=1):
        payload = {"title": title, "body": body, "userId": user_id}
        return self.post("/posts", json=payload)

    def update_post(self, post_id, title=None, body=None):
        payload = {}
        if title:
            payload["title"] = title
        if body:
            payload["body"] = body
        return self.put(f"/posts/{post_id}", json=payload)
