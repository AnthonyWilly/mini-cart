# Open issues

## #1 Total still discounted after removing a coupon (bug)

**Steps to reproduce**

```python
from cart import Cart

cart = Cart()
cart.add_item("book", 100.00)
cart.apply_coupon("SAVE25")
print(cart.total())   # 75.0  (expected)
cart.remove_coupon()
print(cart.total())   # 75.0  (expected: 100.0)
```

**Expected:** after `remove_coupon()` the total goes back to the full subtotal.
**Actual:** the discount is still applied.

## #2 Coupon is not updated when items change (enhancement)

If items are added or removed after a coupon is applied, the discount should
follow the new subtotal.

## #3 Add `expires_on` to coupons (enhancement)

Expired coupons should be rejected with a clear error.
