from src.api_client.client import ApiClient
from jsonschema import validate
from src.schema.Schema import *
from faker import Faker

class TestLogin:
    fake_email = Faker().email()
    
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
        
    def test_invalid_login(self):
        api = ApiClient()
        payload = {
            "email" : "invalidemail",
            "password" : "invalidpassword"
        }
        response = api.post("/verifyLogin", data=payload)
        responseCode = response['responseCode']
        message = response['message']
        
        assert responseCode == 404
        assert str(message).lower().__contains__("user not found")
        validate(response, post_invalid_login_schema)    
        
    def test_create_user(self):
        api = ApiClient()
        payload = {
            'name': 'Test Name',
            'email': self.fake_email,
            'password': 'test',
            'title': 'Mr',
            'birth_date': '12',
            'birth_month': '1',
            'birth_year': '1967',
            'firstname': 'First Name',
            'lastname': 'Last Name',
            'company': 'Company',
            'address1': 'Address 1',
            'address2': 'Address 2',
            'country': 'Country',
            'zipcode': 'Zip code',
            'state': 'State',
            'city': 'City',
            'mobile_number': '1234567890'}
        response = api.post("/createAccount", data=payload)
        responseCode = response['responseCode']
        message = response['message']
        
        assert responseCode == 201
        assert str(message).lower().__contains__("user created")
        validate(response, post_create_user_schema)
    
    def test_update_user(self):
        api = ApiClient()
        payload = {
            'name': 'Test Name 01',
            'email': self.fake_email,
            'password': 'test',
            'title': 'Mr',
            'birth_date': '12',
            'birth_month': '1',
            'birth_year': '1967',
            'firstname': 'First Name',
            'lastname': 'Last Name',
            'company': 'Company',
            'address1': 'Address 1',
            'address2': 'Address 2',
            'country': 'Country',
            'zipcode': 'Zip code',
            'state': 'State',
            'city': 'City',
            'mobile_number': '1234567890'}
        response = api.put("/updateAccount", data=payload)
        responseCode = response['responseCode']
        message = response['message']
        
        assert responseCode == 200
        assert str(message).lower().__contains__("user updated")
        validate(response, post_update_user_schema)
    
    def test_delete_user(self):
        api = ApiClient()
        payload = {
            'email': self.fake_email,
            'password': 'test'
        }
        response = api.delete("/deleteAccount", data=payload)
        responseCode = response['responseCode']
        message = response['message']
        
        assert responseCode == 200
        assert str(message).lower().__contains__("account deleted")
        validate(response, delete_user_schema)
        