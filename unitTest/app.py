import sqlite3 as lite


class ShoppingChart(object):
    def __init__(self, item):
        self.item = item

    def addItem(self):
        print(self.item)


item = ['apple', 'banana']
app = ShoppingChart(item)
app.addItem()
