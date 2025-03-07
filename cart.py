## Import the Product class from product

## Create class Cart

class Cart:
    def __init__(self):
        self.items_in_cart = []
        
    def add_item(self, product, quantity):
        if quantity <= product.quantity:
            self.items_in_cart.append({"Product": product, "Quantity": quantity})
            product.update_quantity(-quantity)
        else:
            print(f"Sorry, we don't have enough {product.name}. We only have {product.quantity} in stock.")
        
    def calculate_cart_values(self):
        total_value = 0
        for item in self.items_in_cart:
            total_value += item["Product"].price * item["Quantity"]
        return total_value
        
    def display_cart(self):
        if not self.items_in_cart:
            print("Your cart is empty.")
        else:
            print("Items in your cart:")
            for item in self.items_in_cart:
                print(f"{item['Product'].name} pcs -> {item['Quantity']}")
