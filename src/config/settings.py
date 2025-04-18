class ConfigManager:
    def __init__(self):
        self.base_url = "https://automationexercise.com/api"
        self.timeout = 30
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
    def update_headers(self, headers):
        self.headers.update(headers)
        