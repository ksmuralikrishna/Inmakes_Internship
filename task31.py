'''Task 31
You are working on a project to develop an e-commerce website. As part of the
project, you need to implement a shopping cart functionality using OOP
concepts in Python. Design and implement the classes for the shopping cart
system with the following requirements:
• The shopping cart should be able to add products, remove products, and
calculate the total price of all the products in the cart.
• Each product should have a name, price, and quantity.
• The shopping cart should be able to handle multiple instances of the same
product and update the quantity accordingly.
• Design the classes and provide the python code implementation for the
shopping cart system.'''

class Product:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        for item in self.products:
            if item.name == product.name:
                item.quantity += product.quantity
                break
        else:
            self.products.append(product)

    def remove_product(self, product_name):
            self.products = [item for item in self.products if item.name != product_name]

    def calculate_total_price(self):
        total_price = sum(item.price * item.quantity for item in self.products)
        return total_price
    
    def display(self):
        if not self.products:
            print("The shopping cart is empty.")
        else:
            result = "Products in the shopping cart:\n"
            for item in self.products:
                result += f"Name: {item.name}, Price: {item.price}, Quantity: {item.quantity}\n"
            return result

cart = ShoppingCart()


cart.add_product(Product("Mouse", 50, 2))
cart.add_product(Product("Keyboard", 50, 3))
cart.add_product(Product("Laptop", 50))



cart.remove_product("Laptop")

s = cart.display()
print(s)
total_price = cart.calculate_total_price()
print("Total price:", total_price)


