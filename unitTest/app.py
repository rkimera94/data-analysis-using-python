from typing import List
import sqlite3 as lite


class ShoppingChart(object):
    def __init__(self, max_size: int):
        self.max_size = max_size
        self.elements: List[str] = []
        global cur
        try:
            con = lite.connect('shopping_cart.db')
            cur = con.cursor()
        except Exception:
            print('unable to create database')

    def createTable(self):
        try:
            cur.execute(
                "create table shopping_chart(id integer primary key,item text,qty integer, user text)"
            )
        except Exception:
            print('Unable to create table')

    def addItem(self, item: str):
        if self.size() == self.max_size:
            raise OverflowError("can not add more items")
        self.elements.append(item)
        print(self.elements)

    def size(self):
        return len(self.elements)

    def fetchItem(self):
        return self.elements

    def deleteItem(self):
        pass

    def totalPrice(self, price_map):
        total_price = 0
        for i in self.elements:
            total_price += price_map.get(i)

        return total_price


item = ['apple', 'banana']
app = ShoppingChart(2)
app.addItem(item)
app.size()


item = ['apple', 'banana']
cart = ShoppingChart(2)

for i in range(len(item)):
    cart.addItem(item[i])


''' test total price calculation'''
item_dict = {'apple': 1.0, 'banana': 2.0}
print(cart.totalPrice(item_dict))
