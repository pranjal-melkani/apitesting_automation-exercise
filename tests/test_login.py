from src.api_client.client import ApiClient
from jsonschema import validate
from src.schema.Schema import *

class TestLogin:
    def test_valid_login(self):
        api = ApiClient()
        payload = {
            "email" : "Testingemail@gmail.com",
            "password" : "test"
        }
        response = api.post("/verifyLogin", data=payload)
        responseCode = response['responseCode']
        message = response['message']
        
        assert responseCode == 200
        assert str(message).lower().__contains__("user exists")
        validate(response, post_valid_login_schema)
        
    def test_login_without_email(self):
        api = ApiClient()
        payload = {
            "password" : "test"
        }
        response = api.post("/verifyLogin", data=payload)
        responseCode = response['responseCode']
        message = response['message']

        assert responseCode == 400
        assert str(message).lower().__contains__("email or password parameter is missing")
        validate(response, post_login_without_email_schema)
        
    def test_delete_to_verify_login(self):
        api = ApiClient()
        response = api.delete("/verifyLogin")
        responseCode = response['responseCode']
        message = response['message']
        
        assert responseCode == 405
        assert str(message).lower().__contains__("this request method is not supported")
        validate(response, delete_to_verify_login_schema)
        