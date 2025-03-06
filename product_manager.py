## Import the Product class from product
from product import Product

## Create class ProductManager

class ProductManager:
    def __init__(self):
        self.products = []
        
    def add_product(self, product):
        self.products.append(product)
        
    def display_products(self):
        if not self.products:
            print("No products to disaply.")
        else:
            for product in self.products:
                print(product.display_info())
                
    def total_products_values(self):
        total_value = 0
        for product in self.products:
            total_value += product.price * product.quantity
        return total_value
        
    