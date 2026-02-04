class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = []

    def add_food(self, food):
        self.menu.append(food)


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name


class Order:
    def __init__(self, order_id, user, restaurant, food_items):
        self.order_id = order_id
        self.user = user
        self.restaurant = restaurant
        self.food_items = food_items
        self.status = "CREATED"
