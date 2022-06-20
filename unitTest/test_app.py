from app import ShoppingChart
import pytest


def test_can_add_item_to_cart():
    item = ['apple']
    cart = ShoppingChart(2)
    cart.addItem(item)
    assert cart.size() == len(item)


def test_item_contains_element():
    item = ['apple']
    cart = ShoppingChart(2)
    cart.addItem(item)
    assert item[0] in cart.fetchItem()[0]


def test_add_max_items_to_cart():
    item = ['apple', 'banana', 'x']
    with pytest.raises(OverflowError):
        cart = ShoppingChart(2)
        for i in range(len(item)):
            cart.addItem(item[i])
