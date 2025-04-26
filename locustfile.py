from locust import HttpUser, task, between
from src.config.settings import ConfigManager
from faker import Faker


class LoadTest(HttpUser):
    wait_time = between(1, 5)
    
    def on_start(self):
        self.config = ConfigManager()
        self.fake_email = f"{Faker().first_name}_{Faker().email}"
    
    @task
    def get_all_brand_list(self):
        url = f"{self.config.base_url}/brandsList"
        self.client.get(url)
    
    @task
    def valid_login(self):
        url = f"{self.config.base_url}/verifyLogin"
        payload = {
            "email" : "Testingemail@gmail.com",
            "password" : "test"
        }
        self.client.post(url, data= payload)
    
    @task
    def create_user(self):
        url = f"{self.config.base_url}/createAccount"
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
        self.client.post(url, data= payload)
      
    @task  
    def update_user(self):
        url = f"{self.config.base_url}/updateAccount" 
        payload = {
            'name': 'Test Name 1.1',
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
        self.client.put(url, data= payload) 
     
    @task   
    def get_user_details(self):
        url = f"{self.config.base_url}/getUserDetailByEmail"
        query_params = {
            'email': "Testemail1@gmail.com",
        }
        self.client.get(url, params= query_params)
        
    @task
    def delete_user(self):
        url = f"{self.config.base_url}/deleteAccount"
        payload = {
            'email': self.fake_email,
            'password': 'test'
        }
        self.client.delete(url, data= payload)
        
        
        
        
        
        
        
        
        
        
        
        