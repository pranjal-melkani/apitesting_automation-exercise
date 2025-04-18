get_all_products_response_schema = {
        "type" : "object",
        "properties" : {
            "responseCode" : {"type" : "number"}, 
            "products" : {"type" : "array"}
        }
}

product_schema = {
    "type" : "object",
    "properties" : {
        "id" : {"type" : "number"},
        "name" : {"type" : "string"}, 
        "price" : {"type" : "string"},
        "brand" : {"type" : "string"},
        "category" : {
            "type" : "object",
            "properties" : {
                "usertype" : {
                    "type" : "object",
                    "properties" : {
                        "usertype" : {"type" : "string"}
                        }
                    },
                "category" : {"type" : "string"}
            }
        }
    }
}

post_all_products_response_schema = {
    "type" : "object",
    "properties" : {
        "responseCode" : {"type" : "number"},
        "message" : {"type" : "string"}
    }
}

get_all_brands_list_schema = {
    "type" : "object",
    "properties" : {
        "responseCode" : {"type" : "number"},
        "brands" : {"type" : "array"}
    }
}

brand_schema = {
    "type" : "object",
    "properties" : {
        "id" : {"type" : "number"},
        "brand" : {"type" : "string"}
    }
}

put_all_brands_schema = {
    "type" : "object",
    "properties" : {
        "responseCode" : {"type" : "number"},
        "message" : {"type" : "string"}
    }    
}

post_search_product_response_schema = {
        "type" : "object",
        "properties" : {
            "responseCode" : {"type" : "number"}, 
            "products" : {"type" : "array"}
        }
}

post_search_product_without_payload_response_schema = {
    "type" : "object",
    "properties" : {
        "responseCode" : {"type" : "number"},
        "message" : {"type" : "string"}
    }
}

post_valid_login_schema = {
    "type" : "object",
    "properties" : {
        "responseCode" : {"type" : "number"},
        "message" : {"type" : "string"}
    }
}

post_login_without_email_schema = {
    "type" : "object",
    "properties" : {
        "responseCode" : {"type" : "number"},
        "message" : {"type" : "string"}
    }
}

delete_to_verify_login_schema = {
    "type" : "object",
    "properties" : {
        "responseCode" : {"type" : "number"},
        "message" : {"type" : "string"}
    }
}

post_invalid_login_schema = {
    "type" : "object",
    "properties" : {
        "responseCode" : {"type" : "number"},
        "message" : {"type" : "string"}
    }
}

post_create_user_schema = {
    "type" : "object",
    "properties" : {
        "responseCode" : {"type" : "number"},
        "message" : {"type" : "string"}
    }
}

delete_user_schema = {
    "type" : "object",
    "properties" : {
        "responseCode" : {"type" : "number"},
        "message" : {"type" : "string"}
    }
}

post_update_user_schema = {
    "type" : "object",
    "properties" : {
        "responseCode" : {"type" : "number"},
        "message" : {"type" : "string"}
    }
}

get_user_details_schema = {
    "type" : "object",
    "properties" : {
        "responseCode" : {"type" : "number"},
        "user" : {
            "type" : "object",
            "properties" : {
                "id" : {"type" : "number"},
                "name" : {"type" : "string"},
                "email" : {"type" : "string"},
                "title" : {"type" : "string"},
                "birth_day" : {"type" : "string"},
                "birth_month" : {"type" : "string"},
                "birth_year" : {"type" : "string"},
                "first_name" : {"type" : "string"},
                "last_name" : {"type" : "string"},
                "company" : {"type" : "string"},
                "address1" : {"type" : "string"},
                "address2" : {"type" : "string"},
                "country" : {"type" : "string"},
                "state" : {"type" : "string"},
                "city" : {"type" : "string"},
                "zipcode" : {"type" : "string"}
            }
        }
    }
}