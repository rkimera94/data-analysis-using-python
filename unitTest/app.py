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

    def createTable(self):
        try:
            cur.execute(
                "create table shopping_chart(id integer primary key,item text,qty integer, user text)"
            )
        except Exception:
            print('Unable to create table')

    def addItem(self):
        print(self.item)

    def fetchItem(self):
        pass

    def deleteItem(self):
        pass


item = ['apple', 'banana']
app = ShoppingChart(item)
app.addItem()
