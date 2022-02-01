# Currently Not used 
import sqlite3
from db.category import Category
from db.db import Db
class Categories:

    def add(self, item : Category): 
        db = Db()
        cur = db.getCursor()
        cur.execute("INSERT INTO categories (id,name) VALUES (?,?)",(item.id,item.name))
        db.close()

    def get(self,id):
        db = Db()
        cur = db.getCursor()
        row = cur.execute("SELECT id,name FROM categories where id = ?", (id)).fetchone()
        item = Category(row[0],row[1])
        db.close()
        return item
    
    def list(self):
        db = Db()
        cur = db.getCursor()
        rows = cur.execute("SELECT id,name FROM categories").fetchall()
        items = []
        for row in rows:
            items.append(Category(row[0],row[1]))
        db.close()
        return items

