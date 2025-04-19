from jsonschema import validate
from src.api_client.client import ApiClient
from src.schema.Schema import *

class TestProducts:
    def test_get_all_products_list(self):
        api = ApiClient()
        response = api.get("/productsList")
        responseCode = response['responseCode']
        products = response['products']
        
        assert responseCode == 200
        assert len(products) >= 1
        validate(response, get_all_products_response_schema)
        for product in products:
            validate(product, product_schema)
            
    def test_post_to_all_products_list(self):
        api = ApiClient()
        response = api.post("/productsList")
        responseCode = response['responseCode']
        message = response['message']
        
        assert responseCode == 405
        assert str(message).lower().__contains__("this request method is not supported")
        validate(response, post_all_products_response_schema)
        
    def test_post_to_search_product(self):
        api = ApiClient()
        payload = {"search_product": "top"}
        response = api.post("/searchProduct", data=payload)
        responseCode = response['responseCode']
        products = response['products']
        
        assert responseCode == 200
        assert len(products) >= 1
        validate(response, post_search_product_response_schema)
        for product in products:
            validate(product, product_schema)
    
    def test_post_to_search_product_without_payload(self):
        api = ApiClient()
        response = api.post("/searchProduct")
        responseCode = response['responseCode']
        message = response['message']
        
        assert responseCode == 400
        assert str(message).lower().__contains__("search_product parameter is missing")
        validate(response, post_search_product_without_payload_response_schema)
    