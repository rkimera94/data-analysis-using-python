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


def test_total_qty():
    cart = ShoppingChart(3)
    cart.addItem('apple')
    cart.addItem('banana')
    price_map = {'apple': 1.0, 'banana': 2.0}
    cart.totalPrice(price_map)
    # print('testing total pricing')
    assert cart.totalPrice(price_map) == 3.0
