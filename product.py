## Create class product

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def display_info(self):
        return f"Product: {self.name} |Price: {self.price:.2f} |Quantity: {self.quantity}"
        
    def update_quantity(self, value):
        self.quantity += value
        if self.quantity < 0:
            self.quantity = 0
            print(f"Quantity for {self.name} can't be smaller than 0.")
