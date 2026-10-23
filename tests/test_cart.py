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


if __name__ == "__main__":
    unittest.main()
