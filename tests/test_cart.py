import unittest

from cart import Cart


class TestCartItems(unittest.TestCase):
    def test_empty_cart_total_is_zero(self):
        self.assertEqual(Cart().total(), 0)

    def test_add_items_and_total(self):
        cart = Cart()
        cart.add_item("book", 20.00, 2)
        cart.add_item("pen", 1.50)
        self.assertEqual(cart.total(), 41.50)

    def test_adding_same_item_increases_quantity(self):
        cart = Cart()
        cart.add_item("pen", 1.50)
        cart.add_item("pen", 1.50, 3)
        self.assertEqual(cart.total(), 6.00)

    def test_remove_item(self):
        cart = Cart()
        cart.add_item("pen", 1.50)
        cart.remove_item("pen")
        self.assertEqual(cart.total(), 0)

    def test_invalid_quantity(self):
        with self.assertRaises(ValueError):
            Cart().add_item("pen", 1.50, 0)


class TestCoupons(unittest.TestCase):
    def test_apply_coupon(self):
        cart = Cart()
        cart.add_item("book", 20.00, 2)
        cart.apply_coupon("SAVE10")
        self.assertEqual(cart.total(), 36.00)

    def test_coupon_is_case_insensitive(self):
        cart = Cart()
        cart.add_item("book", 100.00)
        cart.apply_coupon("save25")
        self.assertEqual(cart.total(), 75.00)

    def test_unknown_coupon(self):
        with self.assertRaises(KeyError):
            Cart().apply_coupon("NOPE")


if __name__ == "__main__":
    unittest.main()
