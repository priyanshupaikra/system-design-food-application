class DeliveryPartner:
    def __init__(self, name):
        self.name = name
        self.available = True


def assign_delivery(order, partners):
    for partner in partners:
        if partner.available:
            partner.available = False
            order.status = "OUT_FOR_DELIVERY"
            print(f"{partner.name} assigned")
            return
