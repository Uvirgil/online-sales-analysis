## Import necesari for the main file

from product import Product
from product_manager import ProductManager
from cart import Cart

## Create the ProductManger insance
product_manager = ProductManager()

product1 = Product("Laptop", 899.99, 56)
product2 = Product("Charger", 19.99, 178)
product3 = Product("Laptop Case", 22.99, 87)
product4 = Product("Keyboard", 35.99, 126)

product_manager.add_product(product1)
product_manager.add_product(product2)
product_manager.add_product(product3)
product_manager.add_product(product4)


product_manager.total_products_values()

## Create Cart instance
cart = Cart()

# cart.add_item(product1, 1)
cart.add_item(product2, 3)
cart.add_item(product3, 2)
cart.add_item(product4, 8)

print("\nCart details:")
cart.display_cart()
cart.calculate_cart_values()
