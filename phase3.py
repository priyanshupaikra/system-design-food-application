# Simple Cache Implementation
class Cache:
    def __init__(self):
        self.store = {}

    def get(self, key):
        return self.store.get(key)

    def set(self, key, value):
        self.store[key] = value

# Usage
# Read-through cache
cache = Cache()

def get_restaurant_menu(restaurant):
    cached = cache.get(restaurant.name)
    if cached:
        print("Menu from cache")
        return cached

    print("Menu from DB")
    cache.set(restaurant.name, restaurant.menu)
    return restaurant.menu
