COUPONS = {
    "SAVE10": 0.10,  # 10% off
    "SAVE25": 0.25,  # 25% off
}


def get_discount_rate(code):
    """Return the discount rate for a coupon code, or raise KeyError."""
    return COUPONS[code.upper()]
