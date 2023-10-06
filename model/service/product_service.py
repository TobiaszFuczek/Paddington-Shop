import re

class ProductService():

    def validate_product_id(self, product_id):
        if re.match(r'^\d{5}$', product_id):
            return product_id
        else:
            return None
    def validate_price(self, price_input):
        if re.match(r'^\d+\.\d{2}$', price_input):
            return float(price_input)
        else:
            return None
