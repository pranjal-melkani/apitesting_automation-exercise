class ConfigManager:
    def __init__(self):
        self.base_url = "https://automationexercise.com/api"
        self.timeout = 30
        self.headers = {}
        
    def update_headers(self, headers):
        self.headers.update(headers)
        