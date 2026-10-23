# mini-cart

A tiny shopping cart library used to practice git workflows.

## Run the tests

```
python -m unittest -v
```

## Usage

```python
from cart import Cart

cart = Cart()
cart.add_item("book", 20.00, 2)
cart.apply_coupon("SAVE10")
print(cart.total())
```
