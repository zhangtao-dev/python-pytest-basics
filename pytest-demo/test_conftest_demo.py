def test_config(global_config):
    assert global_config["base_url"] == "https://api.example.com"
    assert global_config["timeout"] == 30

def test_user(test_user):
    assert test_user["name"] == "admin"
    assert test_user["password"] == "123456"