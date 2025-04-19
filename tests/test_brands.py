from src.api_client.client import ApiClient
from jsonschema import validate
from src.schema.Schema import *

class TestBrands:
    def test_get_all_brands_list(self):
        api = ApiClient()
        response = api.get("/brandsList")
        responseCode = response['responseCode']
        brands = response['brands']
        
        assert responseCode == 200, "Expected response code: 200"
        assert len(brands) >= 1, "No brand found"
        validate(response, get_all_brands_list_schema)
        for brand in brands:
            validate(brand, brand_schema)
            
    def test_put_all_brands_list(self):
        api = ApiClient()
        response = api.put("/brandsList")
        responseCode = response['responseCode']
        message = response['message']
        
        assert responseCode == 405, "Expected response code: 405"
        assert str(message).lower().__contains__("this request method is not supported"), \
            "Expected 'This request method is not supported' message"
        validate(response, put_all_brands_schema)