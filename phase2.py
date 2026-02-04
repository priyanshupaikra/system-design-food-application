# Order lifecycle
# Stateful service

class OrderService:
    def __init__(self):
        self.orders = {}
        self.order_counter = 1

    def place_order(self, user, restaurant, food_items):
        order = Order(self.order_counter, user, restaurant, food_items)
        self.orders[self.order_counter] = order
        self.order_counter += 1
        print(f"Order {order.order_id} placed")
        return order
