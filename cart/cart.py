class Cart:
    """A tiny shopping cart."""

    def __init__(self):
        self.items = {}  # name -> (unit_price, quantity)

    def add_item(self, name, unit_price, quantity=1):
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        if name in self.items:
            price, qty = self.items[name]
            self.items[name] = (price, qty + quantity)
        else:
            self.items[name] = (unit_price, quantity)

    def remove_item(self, name):
        self.items.pop(name, None)

    def subtotal(self):
        return round(sum(p * q for p, q in self.items.values()), 2)

    def total(self):
        return self.subtotal()
