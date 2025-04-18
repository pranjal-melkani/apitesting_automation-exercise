from src.api_client.client import ApiClient
from jsonschema import validate
from src.schema.Schema import *

class TestBrands:
    def test_get_all_brands_list(self):
        api = ApiClient()
        response = api.get("/brandsList")
        responseCode = response['responseCode']
        brands = response['brands']
        
        assert responseCode == 200
        assert len(brands) >= 1
        validate(response, get_all_brands_list_schema)
        for brand in brands:
            validate(brand, brand_schema)