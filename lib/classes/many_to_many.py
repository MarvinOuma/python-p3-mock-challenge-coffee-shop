class Coffee:
    def __init__(self, name):
        self.name = name
        self.orders = []
        
    def add_order(self, order):
        self.orders.append(order)
        
    def num_orders(self):
        return len(self.orders)
    
    def average_price(self):
        if not self.orders:
            return 0
        total_price = sum(order.price for order in self.orders)
        return total_price / len(self.orders)

class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []
        
    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        self.orders.append(order)
        coffee.add_order(order)
        return order
    
    def total_spent(self):
        return sum(order.price for order in self.orders)

class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price