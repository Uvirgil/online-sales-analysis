## Import necesari for the main file

from product import Product
from product_manager import ProductManager

## Create the ProductManger insance
product_manager = ProductManager()

product1 = Product("Phone", 899.99, 56)
product2 = Product("Charger", 9.99, 242)
product3 = Product("Wireless Charger", 19.99, 123)
product4 = Product("Phone Case", 5.99, 432)

product_manager.add_product(product1)
product_manager.add_product(product2)
product_manager.add_product(product3)
product_manager.add_product(product4)

print("Products available:")
product_manager.display_products()