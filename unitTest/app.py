import sqlite3 as lite


class ShoppingChart(object):
    def __init__(self, item):
        self.item = item
        global cur
        try:
            con = lite.connect('shopping_cart.db')
            cur = con.cursor()
        except Exception:
            print('unable to create database')

    def addItem(self):
        print(self.item)

    def fetchItem(self):
        pass

    def deleteItem(self):
        pass


item = ['apple', 'banana']
app = ShoppingChart(item)
app.addItem()
