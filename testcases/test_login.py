import pytest
from api.user_api import UserAPI
from utils.assert_util import assert_status_code, assert_json_value

user_api = UserAPI()

def test_user_login_success():
    response = user_api.login("admin", "123456")
    assert_status_code(response, 201)
    assert_json_value(response, "title", "admin")
    assert_json_value(response, "body", "123456")