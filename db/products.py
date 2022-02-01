import sqlite3
from db.product import Product
from db.db import Db
class Products:

    def add(self, item : Product): 
        db = Db()
        cur = db.getCursor()
        cur.execute("INSERT INTO products (name, category_id, category_name,price, available_quantity, warning_quantity) VALUES (?,?,?,?,?)",
                    (item.id, item.name, item.category_id, item.category_name, item.price, item.available_quantity, item.warning_quantity))
        db.close()

    def get(self,id):
        db = Db()
        cur = db.getCursor()
        row = cur.execute("SELECT id,name, category_id, category_name,price, available_quantity, warning_quantity FROM products where id = ?", (id)).fetchone()
        item = Product(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
        db.close()
        return item
    
    def list(self):
        db = Db()
        cur = db.getCursor()
        rows = cur.execute("SELECT id,name, category_id,category_name, price, available_quantity, warning_quantity FROM products").fetchall()
        items = []
        for row in rows:
            items.append(Product(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
        db.close()
        return items
    
    def addQuantity(self,id,qty):
        db = Db()
        cur = db.getCursor()
        cur.execute("UPDATE products SET available_quantity = (available_quantity + ?) where id = ?", (qty,id))
        db.close()

