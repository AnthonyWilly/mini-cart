from .coupons import get_discount_rate


class Cart:
    """A tiny shopping cart."""

    def __init__(self):
        self.items = {}  # name -> (unit_price, quantity)
        self.coupon = None
        self.discount = 0.0

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

    def apply_coupon(self, code):
        rate = get_discount_rate(code)
        self.coupon = code.upper()
        self.discount = round(self.subtotal() * rate, 2)

    def remove_coupon(self):
        self.coupon = None

    def subtotal(self):
        return round(sum(p * q for p, q in self.items.values()), 2)

    def total(self):
        return round(self.subtotal() - self.discount, 2)
