from shopping_cart import ShoppingCart


def test_can_add_item_to_cart():
    cart = ShoppingCart()
    cart.add("apple")
    assert cart.size() == 1


def test_when_item_add_then_cart_contains_item():
    cart = ShoppingCart()
    cart.add("apple")
    pass