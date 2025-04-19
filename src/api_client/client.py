import requests
from ..config.settings import ConfigManager

class ApiClient:
    def __init__(self):
        self.config = ConfigManager()
        
    def get(self, endpoint, query_parameters=None):
        url = f"{self.config.base_url}{endpoint}"
        try:
            response = requests.get(
                url,
                headers = self.config.headers,
                params = query_parameters,
                timeout = self.config.timeout
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise Exception(f"GET request failed: {str(e)}")
        
    def post(self, endpoint, data=None, json=None, query_parameters=None):
        url = f"{self.config.base_url}{endpoint}"
        try:
            response = requests.post(
                url = url,
                headers = self.config.headers,
                data = data,
                json = json,
                params = query_parameters,
                timeout = self.config.timeout
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise Exception(f"POST request failed: {str(e)}")
        
    def put(self, endpoint, data=None, json=None, query_parameters=None):
        url = f"{self.config.base_url}{endpoint}"
        try:
            response = requests.put(
                url = url,
                data = data,
                headers = self.config.headers,
                params = query_parameters,
                json = json,
                timeout = self.config.timeout
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise Exception(f"PUT request failed: {str(e)}")
        
    def delete(self, endpoint, data=None, json=None, query_parameters=None):
        url = f"{self.config.base_url}{endpoint}"
        try:
            response = requests.delete(
                url,
                headers= self.config.headers,
                data= data,
                json= json,
                params= query_parameters,
                timeout= self.config.timeout
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise Exception(f"DELETE request failed: {str(e)}")