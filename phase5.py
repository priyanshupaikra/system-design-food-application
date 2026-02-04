# Simple Queue (like Kafka / SQS logic)
from collections import deque

class MessageQueue:
    def __init__(self):
        self.queue = deque()

    def publish(self, message):
        self.queue.append(message)

    def consume(self):
        if self.queue:
            return self.queue.popleft()

# Order Processing Worker
queue = MessageQueue()

def process_orders():
    while True:
        order = queue.consume()
        if not order:
            break
        order.status = "CONFIRMED"
        print(f"Order {order.order_id} confirmed")
